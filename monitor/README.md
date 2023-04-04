# Sys montioring

Compose file starts up:
- Prometheus
- Node exporter
- Alertmanager


# Starting up
Go to root of this project (the directory containing this README)    
Change `.env` file.  
Do `docker-compose up -d`

# Details
- Prometheus is started as `network_mode=host` for now, this helps it scrap targets on localhost without being on same network as them  

