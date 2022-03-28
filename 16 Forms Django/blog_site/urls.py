from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('kontak/', views.contact),
    path('blogs/', include('blogs.urls', namespace='blogs')),
    path('admin/', admin.site.urls),
]