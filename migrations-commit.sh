cd /qureupdate/misc

echo "running migration "

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