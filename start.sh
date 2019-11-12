#!/bin/bash

export PYTHONOPTIMIZE=1
source /ddhome/cmdb/venv/bin/activate
uwsgi --http :9000 --wsgi-file cmdb/wsgi.py --master --processes 4 --threads 2 --daemonize=/ddhome/cmdb/logs/uwsgi.log
celery multi start schdue -A scheduler -l info --pidfile=scheduler.pid --logfile=logs/scheduler%I.log
nohup celery beat -A scheduler -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler >> logs/beat.log &
