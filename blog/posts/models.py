# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from register.models import User

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, blank=True, null=False, default=None)
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=False, default=None)
    briefly_description = models.TextField(blank=True, null=False, default=None)
    comments_count = models.IntegerField()
    likes_count = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "Author: %s Title: %s Briefly description: %s" % (self.author, self.title,
                                                                 self.briefly_description)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

class ImagePost(models.Model):
    post = models.ForeignKey(Post, blank=True, null=False, default=None)
    url_path = models.ImageField(upload_to='')

    def __str__(self):
        return "Image id: %s" % self.id

    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photos"