from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('blogs/', include('blogs.urls')),
    path('', views.index),
    path('admin/', admin.site.urls),
]
