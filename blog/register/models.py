# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField()
    password = models.CharField(max_length=64)

    def __str__(self):
        return "Name: %s LastName: %s Email %s" % (self.name, self.last_name, self.email)

    class Meta:
        verbose_name = "Blog User"
        verbose_name_plural = "Blog Users"