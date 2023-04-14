set -a



cd /qureupdate/apihub/
source psql.env

echo $POSTGRES_USER
echo $POSTGRES_PASSWORD

cd /qureupdate/misc/


docker exec -it psql psql -U postgres -c "CREATE DATABASE apihub;"
docker exec -it psql psql -U postgres -c "CREATE DATABASE cxr_api;"

PGPASSWORD=$POSTGRES_PASSWORD pg_restore --no-password -h 127.0.0.1 -p 5432 -U postgres -d cxr_api -v "cxr.backup" > cxr_restore.log 2>&1
PGPASSWORD=$POSTGRES_PASSWORD pg_restore --no-password -h 127.0.0.1 -p 5432 -U postgres -d apihub -v "api.backup" > apihub_restore.log 2>&1


#PGPASSWORD=$POSTGRES_PASSWORD pg_restore -h 127.0.0.1 -p 5432 -U postgres -d cxrapi -v "cxr.backup"
