#!/usr/bin/env bash
#set -e
#export PATH=/home/qureai_support/bin:/home/qureai_support/.local/bin:$PATH

cd /qureupdate

echo "gateway Deployment started"

docker exec -it psql psql -U postgres -c "CREATE DATABASE dcmio;"


docker-compose -p gateway -f gateway/docker-compose.yml down --remove-orphans | true
docker-compose -p gateway -f gateway/docker-compose.yml up -d

echo " gateway Deployment complete"