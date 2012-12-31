from celery import task
from django.conf import settings

import os;

@task()
def addWebsite(site):
    os.system(settings.PROJECT_DIR + '../scripts/create-site.sh ' + site.slug)
    site.created = True;
    site.save()
    return site
