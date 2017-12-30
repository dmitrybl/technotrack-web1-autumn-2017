# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.db.models import Q

from .forms import PostForm
from .models import Post

# Create your views here.
def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect("posts:post_list")
    context = {
        "form": form,
    }
    return render(request, "post_form.html", context)

def post_detail(request, id = None):
    instance = get_object_or_404(Post, id = id)
    context = {
        "title": instance.title,
        "instance": instance
    }
    return render(request, "post_detail.html", context)

def post_list(request):
    queryset_list = Post.objects.all().order_by("-updated")

    query = request.GET.get("s")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query))
    paginator = Paginator(queryset_list, 3)
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        "object_list": queryset,
        "title": "List"
    }
    return render(request, "post_list.html", context)

def post_update(request, id = None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance = instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect("posts:post_list")

    context = {
        "title": instance.title,
        "instance": instance,
        "form": form
    }
    return render(request, "post_update.html", context)

def post_delete(request, id = None):
    instance = get_object_or_404(Post, id = id)
    instance.delete()
    return redirect("posts:post_list")
