from django.conf.urls import url, include
from django.contrib import admin
from core import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^apps/$', views.AppsList.as_view(), name='core/my_apps'),
    url(r'^apps/new/$', login_required(views.NewAppPost.as_view()), name='core/new_app_post'),
    url(r'^apps/(?P<pk>\d+)/$', views.AppDetail.as_view(), name='core/app_post_detail'),
]

