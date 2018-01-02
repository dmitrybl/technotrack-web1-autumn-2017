# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.db.models import Q

from comments.forms import CommentForm
from comments.models import Comment
from .forms import PostForm
from .models import Post

# Create your views here.
def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect("posts:post_list")
    context = {
        "form": form,
    }
    return render(request, "post_form.html", context)

def post_detail(request, id = None):
    instance = get_object_or_404(Post, id = id)

    initial_data = {
        "content_type": instance.get_content_type,
        "object_id": instance.id
    }

    form = CommentForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        c_type = form.cleaned_data.get("content_type")
        content_type = ContentType.objects.get(model=c_type)
        obj_id = form.cleaned_data.get("object_id")
        content_data = form.cleaned_data.get("content")
        parent_obj = None
        try:
            parent_id = int(request.POST.get("parent_id"))
        except:
            parent_id = None

        if parent_id:
            parent_qs = Comment.objects.filter(id = parent_id)
            if parent_qs.exists() and parent_qs.count() == 1:
                parent_obj = parent_qs.first()


        new_comment, created = Comment.objects.get_or_create(
                                    user = request.user,
                                    content_type = content_type,
                                    object_id = obj_id,
                                    content = content_data,
                                    parent = parent_obj,
                                )
        return HttpResponseRedirect(new_comment.content_object.get_absolute_url())


    comments = instance.comments
    context = {
        "title": instance.title,
        "instance": instance,
        "comments": comments,
        "comment_form": form,
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
    instance = get_object_or_404(Post, id = id)
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
