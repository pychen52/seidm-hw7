#!/bin/bash

NAME="drf"
DIR=/home/yeeede/seidm-hw7/drf
USER=yeeede
GROUP=yeeede
WORKERS=3
BIND=unix:/home/yeeede/pyenv/run/gunicorn.sock
# BIND=0.0.0.0:8000
DJANGO_SETTINGS_MODULE=drf.settings
DJANGO_WSGI_MODULE=drf.wsgi
LOG_LEVEL=error

cd /home/yeeede/seidm-hw7/drf
source /home/yeeede/pyenv/bin/activate

export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=/home/yeeede/pyenv/bin/:$PYTHONPATH

exec /home/yeeede/pyenv/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $WORKERS \
  --user=$USER \
  --group=$GROUP \
  --bind=$BIND \
  --log-level=$LOG_LEVEL \
  --log-file=-
