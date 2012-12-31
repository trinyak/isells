from django.conf.urls import patterns, url

urlpatterns = patterns('shop.views',
    url(r'^$', 'create'),
    url(r'^wait', 'wait')
)