# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import reverse
from django.views.generic import ListView, CreateView, DetailView
from posts.models import Post
from django import forms


# Create your views here.

class AppForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = 'title', 'description', 'briefly_description'

class AppsList(ListView):
    template_name = 'core/my_apps.html'
    context_object_name = 'apps'
    model = Post


class NewAppPost(CreateView):
    template_name = 'core/new_app_post.html'
    form_class = AppForm

    def get_success_url(self):
        return reverse('core:app_post_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(NewAppPost, self).form_valid(form)


class AppDetail(DetailView):
    template_name = 'core/app_post_detail.html'
    context_object_name = 'app'
    model = Post
