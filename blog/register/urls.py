from django.conf.urls import url, include
from django.contrib import admin
from register import views

urlpatterns = [
    url(r'^register/', views.register, name='register')
]