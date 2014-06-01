from django.conf.urls import patterns, include, url
from django.shortcuts import render
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    (r'^$', render,
            { 'template': 'index.html' }, 'index'),
)
