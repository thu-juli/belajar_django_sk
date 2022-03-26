from django.urls import path
from django.conf.urls import handler404
from . import views


urlpatterns = [
    path('<int:id>', views.single),
    path('', views.index),
]

handler404 = 'blogs.views.handler404'
