from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('blogs/<str:author>/<int:page>/',
         include('blogs.urls', namespace='article')),
    path('admin/', admin.site.urls),
]
