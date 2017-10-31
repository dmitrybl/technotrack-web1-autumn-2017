from django.conf.urls import url, include
from django.contrib import admin
from posts import views

urlpatterns = [
    url(r'^posts/', views.posts, name='posts')
]