from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.


def comments(request, name=None):
    return render(request, 'comments.html', {'name': name})