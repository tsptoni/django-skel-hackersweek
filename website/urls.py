# -*- coding: utf-8 -*-
# Urls of your app.

from django.conf.urls import patterns, url

urlpatterns = patterns('website.views',
    url(r'^$', 'index', name='index'),
)
