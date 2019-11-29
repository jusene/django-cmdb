#!/bin/bash

export PYTHONOPTIMIZE=1
kill `pidof uwsgi`
source /ddhome/cmdb/venv/bin/activate
uwsgi --http :9000 --wsgi-file cmdb/wsgi.py --master --processes 4 --threads 2 --daemonize=/ddhome/cmdb/logs/uwsgi.log
celery multi restart schdue -A scheduler -l info -O OPTIMIZATION --pidfile=scheduler.pid --logfile=logs/scheduler%I.log
kill `cat celerybeat.pid`
#nohup celery beat -A scheduler -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler >> logs/beat.log & 
nohup celery beat -A scheduler -l info > logs/beat.log &
