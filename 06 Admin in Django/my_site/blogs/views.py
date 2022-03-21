from django.http import HttpResponse
from .models import Blog


def index(request):
    # noinspection PyUnresolvedReferences
    blogs = Blog.objects.all()
    output = ', '.join([str(blog) for blog in blogs])
    return HttpResponse(output)
