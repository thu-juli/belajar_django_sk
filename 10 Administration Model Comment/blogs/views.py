from django.shortcuts import render
from .models import Blog


def index(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs/index.html', {'blogs': blogs})
