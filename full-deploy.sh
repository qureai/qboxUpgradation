set -e

echo "taking backups of cxr and apihub"

cd /qureupdate/misc
bash pgbackup.sh

echo "changing yml and env files"

python3 envchange.py
python3 ymlchange.py

cd /qureupdate

echo "removing previous dockers"

docker ps -a | awk '{print $1}' | while read in; do docker rm -f $in; done

bash deploy-cxr.sh
bash deploy-gateway.sh
bash deploy-monitoring.sh

echo "Deployment complete"

echo "restoring database"

cd /qureupdate/misc

bash pgrestore.sh

echo "restoring database complete"


echo "running migration complete"

docker cp apihubmigrate.sh  apihub:/srv/apihub/authentication/
docker exec apihub bash /srv/apihub/authentication/apihubmigrate.sh

echo "apihub migration complete"




docker cp cxrmigrate.sh  cxr_api:/srv/cxr_api/cxr_api/
docker exec cxr_api bash /srv/cxr_api/cxr_api/cxrmigrate.sh

echo "cxr migration complete"

echo "apihub commit"

cd /qureupdate/apihub

set -a
source .env

echo $APIHUB_TAG

docker commit apihub qureai/apihub:$APIHUB_TAG

echo "apihub commit done"

echo "migration complete"

docker logout
cd /qureupdate

python3 notification.py "installation completed"
