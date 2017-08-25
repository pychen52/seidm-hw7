#!/bin/bash

NAME="drf"
DIR=/home/peiyuan/seidm-hw7/drf
USER=peiyuan
GROUP=peiyuan
WORKERS=3
BIND=unix:/home/peiyuan/pyenv/run/gunicorn.sock
#BIND=0.0.0.0:8000
DJANGO_SETTINGS_MODULE=drf.settings
DJANGO_WSGI_MODULE=drf.wsgi
LOG_LEVEL=error

cd /home/peiyuan/seidm-hw7/drf
source /home/peiyuan/pyenv/bin/activate

export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=/home/yeeede/pyenv/bin/:$PYTHONPATH

exec /home/peiyuan/pyenv/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $WORKERS \
  --user=$USER \
  --group=$GROUP \
  --bind=$BIND \
  --log-level=$LOG_LEVEL \
  --log-file=-
