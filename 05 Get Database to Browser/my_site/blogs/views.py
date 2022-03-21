from .models import Blog
from django.http import HttpResponse


def index(request):
    # noinspection PyUnresolvedReferences
    blogs = Blog.objects.all()
    output = ', '.join([str(blog) for blog in blogs])
    return HttpResponse(output)
