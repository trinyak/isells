from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from datetime import datetime

class Plan(models.Model):
    name = models.CharField(max_length=30)
    slug = AutoSlugField(populate_from='name', unique=True, always_update=True, editable=True, blank=True)
    price = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name


class Website(models.Model):
    name = models.CharField(max_length=30)
    slug = AutoSlugField(populate_from='name', unique=True, always_update=True, editable=True, blank=True)
    user = models.ForeignKey(User)
    plan = models.ForeignKey(Plan)
    domain = models.CharField(max_length=255, default="")
    created = models.BooleanField(default=False)
    date_add = models.DateTimeField(default=datetime.now, auto_now_add=True, blank=True)
    date_mod = models.DateTimeField(default=datetime.now, auto_now=True, blank=True)

    def __unicode__(self):
        return self.name + ' [' + self.domain + ']'


class Subscriptions(models.Model):
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    plan = models.ForeignKey(Plan)
    website = models.ForeignKey(Website)

