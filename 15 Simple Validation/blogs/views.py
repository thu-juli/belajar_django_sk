from django.shortcuts import render
from .models import Blog
from django.http import HttpResponseRedirect


def index(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs/index.html', {'blogs': blogs})


def single(request, id):
    blog = Blog.objects.get(pk=id)
    return render(request, 'blogs/single.html', {'blog': blog})


def comment(request, id):
    blog = Blog.objects.get(pk=id)

    if request.method == 'POST':
        new_desc = request.POST['desc']

        if len(new_desc) < 10:
            return render(request, 'blogs/single.html',
                          {
                              'blog': blog,
                              'errors': 'komentar minimal 10 karakter',
                          })

        blog.comment_set.create(desc=new_desc)
        return HttpResponseRedirect('/blogs')

# def comment(request, id):
#     blog = Blog.objects.get(pk=id)
#     if request.method == 'POST':
#         new_desc = request.POST['desc']
#         blog.comment_set.create(desc=new_desc)
#         return HttpResponseRedirect('/blogs')
