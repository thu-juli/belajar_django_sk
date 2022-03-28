from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('kontak/', views.contact, name='contact'),
    path('blogs/', include('blogs.urls', namespace='blogs')),
    path('admin/', admin.site.urls),
]
