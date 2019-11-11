#!/bin/bash

kill `pidof uwsgi`
source /ddhome/cmdb/venv/bin/activate
uwsgi --http :9000 --wsgi-file cmdb/wsgi.py --master --processes 4 --threads 2 --daemonize=/ddhome/cmdb/logs/uwsgi.log
