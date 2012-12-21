from django.conf.urls import patterns, include, url
from django.contrib import admin
from cms.sitemaps import CMSSitemap
from registration.forms import RegistrationFormUniqueEmail
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': {'cmspages': CMSSitemap}}),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^', include('cms.urls')),
)

#if settings.DEBUG:
#    urlpatterns = patterns('',
#        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
#            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
#        url(r'', include('django.contrib.staticfiles.urls')),
#    ) + urlpatterns