from django.conf.urls import url
from django.contrib import admin

from posts.views import *


urlpatterns = [
    url(r'^$', post_list, name = 'post_list'),
    url(r'^create/$', post_create, name = 'post_create'),
    url(r'^(?P<id>[\d]+)/$', post_detail, name = "post_detail"),
    url(r'^(?P<id>[\d]+)/edit/$', post_update, name = 'post_update'),
    url(r'^(?P<id>[\d]+)/delete/$', post_delete, name = 'post_delete'),
]