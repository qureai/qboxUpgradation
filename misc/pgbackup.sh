set -a
source var.py
cp $psqlenv /qureupdate/misc/psql.env

cd /qureupdate/misc/
source psql.env

echo $POSTGRES_USER
echo $POSTGRES_PASSWORD

PGPASSWORD=$POSTGRES_PASSWORD pg_dump -h 127.0.0.1 -p 5432 -U postgres  -F c -b -v -f  "cxr.backup" cxr_api || PGPASSWORD=$POSTGRES_PASSWORD pg_dump -h 127.0.0.1 -p 5432 -U postgres  -F c -b -v -f  "cxr.backup" cxrapi
PGPASSWORD=$POSTGRES_PASSWORD pg_dump -h 127.0.0.1 -p 5432 -U postgres  -F c -b -v -f  "api.backup" apihub