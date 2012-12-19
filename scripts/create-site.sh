#!/bin/sh

mkdir /data/projects/medtest
cd /data/projects/medtest
mkdir static
mkdir media
mkdir logs
sudo chown -R www-data:www-data /data/projects/medtest

backup_dir1(){
   cd /data/projects/medtest;
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
        'NAME': 'medtest',
        'USER': 'root',
        'PASSWORD': 'baster551737',
        'HOST': 'isells.cbiec5vjmqef.us-east-1.rds.amazonaws.com',
        'PORT': '',
    }
}
" > local_settings.py
  mysql -h isells.cbiec5vjmqef.us-east-1.rds.amazonaws.com -uroot -pbaster551737 -e "DROP DATABASE IF EXISTS medtest"
  mysql -h isells.cbiec5vjmqef.us-east-1.rds.amazonaws.com -uroot -pbaster551737 -e "CREATE DATABASE medtest CHARACTER SET='utf8'"
  python manage.py syncdb --migrate --noinput
  #python manage.py createsuperuser --username=admin --email=a@dmin.com
  echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@isells.eu', '551737')" | python manage.py shell
}

export -f backup_dir1

su www-data -c "bash -c backup_dir1"

echo '
server {
    listen  80;
    server_name medtest.isells.eu;
    access_log /data/projects/medtest/logs/nginx_access.log;
    error_log /data/projects/medtest/logs/nginx_error.log;

    location / {
        uwsgi_pass  unix:///var/run/uwsgi/app/medtest/socket;
        include     uwsgi_params;
    }

    location /media/  {
        alias /data/projects/medtest/media/;
    }

    location  /static/ {
        alias /data/projects/medtest/static/;
    }
}
' > /etc/nginx/sites-enabled/medtest

echo '
[uwsgi]
vhost = true
plugins = python
master = true
enable-threads = true
processes = 2
wsgi-file = /data/projects/medtest/django-shop/core/wsgi.py
virtualenv = /data/projects/medtest/env
chdir = /data/projects/medtest/django-shop/
touch-reload = /data/projects/medtest/django-shop/reload
' > /etc/uwsgi/apps-enabled/medtest.ini

service nginx reload
service uwsgi restart

exit 0