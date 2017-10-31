from django.conf.urls import url, include
from django.contrib import admin
from comments import views

urlpatterns = [
    url(r'^comments/', views.comments, name='comments')
]