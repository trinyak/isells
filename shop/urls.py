from django.conf.urls import patterns, url

urlpatterns = patterns('shop.views',
    url(r'^create', 'create'),
    url(r'^wait/(?P<site_id>\d+)/$', 'wait'),
    url(r'^check_status/(?P<site_id>\d+)/$', 'check_status'),
)