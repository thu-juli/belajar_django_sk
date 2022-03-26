from django.shortcuts import get_object_or_404, render
from .models import Blog


def handler404(request, exception):
    return render(request, 'blogs/not_found.html', status=404)


def index(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs/index.html', {'blogs': blogs})


def single(request, id):
    blog = get_object_or_404(Blog, pk=id)
    return render(request, 'blogs/layout.html', {'blog': blog})
