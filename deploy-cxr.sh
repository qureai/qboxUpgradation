#!/usr/bin/env bash
set -e
# for latest docker compose
#export PATH=/home/qureai_support/bin:/home/qureai_support/.local/bin:$PATH

cd /qureupdate
echo "Deployment started"

#sudo aws ecr get-login --no-include-email --region=ap-south-1 | /bin/bash
# aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin awsqure.dkr.ecr.ap-south-1.amazonaws.com

docker volume create --name=qxr-checkpoints | true
docker volume create --name=qxr-data | true
docker volume create --name=qxr-notebooks | true
docker volume create --name=apihub-data | true
docker volume create --name=apihub-notebooks | true
docker volume create --name=psql-data | true
docker volume create --name=psql-data1 | true
docker volume create --name=dcmio-data | true
docker volume create --name=dcmio-notebooks | true
docker volume create --name=prometheus-data | true
docker volume create --name=alertmanager-data | true



echo "deploying dockers"


docker-compose -p apihub -f apihub/apihub.yml down --remove-orphans | true
docker-compose -p apihub -f apihub/apihub.yml up -d

docker-compose -p cxr -f cxr/cxr.yml down --remove-orphans | true
docker-compose -p cxr -f cxr/cxr.yml up -d

docker-compose -p workers -f cxr/workers.yml down --remove-orphans | true
docker-compose -p workers -f cxr/workers.yml up -d

echo "Deployment complete"