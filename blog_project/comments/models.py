# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from core.models import User
from posts.models import Post

# Create your models here.

class Comment(models.Model):
    author = models.ForeignKey(User, blank=True, null=False, default=None)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    post = models.ForeignKey(Post, blank=True, null=False, default=None)
    content = models.TextField(blank=True, null=False, default=None)

    def __str__(self):
        return "Author: %s Date: %s" % (self.author, self.created_date)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"