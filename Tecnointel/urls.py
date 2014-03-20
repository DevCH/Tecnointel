from django.conf.urls import patterns, include, url
# from django.conf.urls.defaults import *
from Tecnointel.views import initServer, holaMundo, now, nowPlus

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Tecnointel.views.home', name='home'),
    # url(r'^Tecnointel/', include('Tecnointel.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

	(r'^$', initServer),
	(r'^holaMundo/$', holaMundo),
	(r'^now/$', now),
	(r'^nowPlus/(\d{1,2})/$', nowPlus),
)
