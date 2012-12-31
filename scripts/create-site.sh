#!/bin/bash

if test -z "$1"
then
    echo "Error: site name is not set!"
    exit 0
else
    SITE_NAME=$1
fi

mkdir /data/projects/${SITE_NAME}
cd /data/projects/${SITE_NAME}
mkdir static
mkdir media
mkdir logs
sudo chown -R www-data:www-data /data/projects/${SITE_NAME}

init_site(){
    cd /data/projects/${SITE_NAME};
    virtualenv --system-site-packages env;
    source env/bin/activate;
    git clone https://github.com/alexzaporozhets/django-shop.git
    cd django-shop
    pip install -r requirements.txt
    python manage.py collectstatic --noinput

echo "
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '${SITE_NAME}',
        'USER': 'root',
        'PASSWORD': 'baster551737',
        'HOST': 'isells.cbiec5vjmqef.us-east-1.rds.amazonaws.com',
        'PORT': '',
    }
}
DEBUG = False
" > local_settings.py

    # creating a database
    mysql -h isells.cbiec5vjmqef.us-east-1.rds.amazonaws.com -uroot -pbaster551737 -e "DROP DATABASE IF EXISTS ${SITE_NAME}"
    mysql -h isells.cbiec5vjmqef.us-east-1.rds.amazonaws.com -uroot -pbaster551737 -e "CREATE DATABASE ${SITE_NAME} CHARACTER SET='utf8'"
    python manage.py syncdb --migrate --noinput
    #python manage.py createsuperuser --username=admin --email=a@dmin.com

    # adding a Django super-user
    echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@${SITE_NAME}.isells.eu', 'admin')" | python manage.py shell

    # importing a demo products
    python manage.py importyml /data/isells.eu/isells/scripts/demo_site_data_yml.xml --images
}

export SITE_NAME=${SITE_NAME}
export -f init_site

su www-data -c "bash -c init_site"

# adding nginx config
echo "
server {
    listen  80;
    server_name ${SITE_NAME}.isells.eu;
    access_log /data/projects/${SITE_NAME}/logs/nginx_access.log;
    error_log /data/projects/${SITE_NAME}/logs/nginx_error.log;

    location / {
        uwsgi_pass  unix:///var/run/uwsgi/app/${SITE_NAME}/socket;
        include     uwsgi_params;
    }

    location /media/  {
        alias /data/projects/${SITE_NAME}/media/;
    }

    location  /static/ {
        alias /data/projects/${SITE_NAME}/static/;
    }
}
" > /etc/nginx/sites-enabled/${SITE_NAME}

# adding uwsgi config
echo "
[uwsgi]
vhost = true
plugins = python
master = true
enable-threads = true
processes = 2
wsgi-file = /data/projects/${SITE_NAME}/django-shop/core/wsgi.py
virtualenv = /data/projects/${SITE_NAME}/env
chdir = /data/projects/${SITE_NAME}/django-shop/
touch-reload = /data/projects/${SITE_NAME}/django-shop/reload
" > /etc/uwsgi/apps-enabled/${SITE_NAME}.ini

service nginx reload
service uwsgi restart

exit 0