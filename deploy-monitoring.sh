#!/usr/bin/env bash
set -e
#export PATH=/home/qureai_support/bin:/home/qureai_support/.local/bin:$PATH

cd /qureupdate

echo "monitor Deployment started"



docker-compose -p monitor -f monitor/docker-compose.yml down --remove-orphans | true
docker-compose -p monitor -f monitor/docker-compose.yml up -d

echo "monitor Deployment complete"