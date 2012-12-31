#!/bin/sh
sudo -i
sudo su www-data -c /bin/bash
cd /data/isells.eu
source env/bin/activate
cd isells
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate

# updating the codebase
git checkout - . && git fetch && git pull --rebase

exit
service uwsgi restart


# python manage.py celery worker --loglevel=info
