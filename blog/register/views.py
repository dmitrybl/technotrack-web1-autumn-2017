# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import RegistrationForm

# Create your views here.

def register(request):
    form = RegistrationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form = form.save()
    return render(request, 'registration.html', locals())
