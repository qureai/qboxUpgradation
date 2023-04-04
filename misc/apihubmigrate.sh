#!/bin/bash
source activate apihub
python3 manage.py migrate

sed -i "s/.*alias \/srv\/data\/cxr\/;.*/add_header Access-Control-Allow-Origin *; alias \/srv\/data\/cxr\/;/g" /etc/nginx/sites-enabled/django_nginx.conf
service nginx restart &
