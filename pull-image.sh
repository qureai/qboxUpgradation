set -e

cd /qureupdate
set -a
source .env

# docker-compose -p apihub -f apihub/apihub.yml pull
# docker-compose -p cxr -f cxr/cxr.yml pull
# docker-compose -p cxr -f cxr/workers.yml pull
# docker-compose -p gateway -f gateway/docker-compose.yml pull
# docker-compose -p monitor -f monitor/docker-compose.yml pull
docker pull qureai/apihub:${APIHUB_TAG}
docker pull redis:${REDIS_TAG}
docker pull postgres:${POSTGRES_TAG}
docker pull qureai/qtrack_web.frontend:${QTRACK_FRONTEND_TAG}
docker pull qureai/qxr_checkpoints:${CHECKPOINTS_TAG}
docker pull qureai/cxr_api:${CXRAPI_TAG}
docker pull qureai/dcmio:${DCMIO_TAG}
docker-compose -p monitor -f monitor/docker-compose.yml pull