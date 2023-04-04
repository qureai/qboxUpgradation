bash /home/qureai_support/deployment/deploy-cxr.sh apihub-26b2609c3996 cxr_api-v3.5.70 qxr_checkpoints-3.2.QXR-348.7_onyx_models_encrypted

bash /home/qureai_support/deployment/deploy-cxr.sh apihub-26b2609c3996 cxr_api-0.1_stable_QXR_379_6_71d0419 qxr_checkpoints-3.2.QXR-379.4_onyx_models_encrypted

bash /home/qureai_support/deployment/deploy-cxr.sh apihub-26b2609c3996 cxr_api-v3.5.70-modified qxr_checkpoints-3.2.QXR-348.7_onyx_models_encrypted

bash /home/qureai_support/deployment/deploy-gateway.sh

TAG=cxr_api-v3.5.70 CHECKPOINTS_TAG=qxr_checkpoints-3.2.QXR-348.7_onyx_models_unencrypted docker compose -p cxr -f cxr/cxr.yml up -d

TAG=cxr_api-v3.5.70 CHECKPOINTS_TAG=qxr_checkpoints-3.2.QXR-348.7_onyx_models_unencrypted docker compose -p workers -f cxr/workers.yml up -d

APIHUB_TAG=apihub-26b2609c3996 docker compose -p apihub -f apihub/docker-compose.yml down

<!-- APIHUB_TAG=apihub-qtrack docker-compose -p apihub -f apihub/docker-compose.yml pull -->
