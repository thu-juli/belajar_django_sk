from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def index(request):
    return HttpResponse('<h1>Home</h1>')


def category(request, categoryInput):
    category = Post.objects.filter(category=categoryInput)
    print(category)
    return HttpResponse('Post Category')


def singlePost(request, slugIput):
    post = Post.objects.get(slug=slugIput)
    title = post.title
    body = post.body
    category = post.category
    return HttpResponse(f'<h1>{title}</h1><p>{body}</p><p><em>{category}</em></p>')
