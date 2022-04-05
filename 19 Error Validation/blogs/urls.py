from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/<str:pk>/', views.blogs, name='blogs'),
    path('create-project/', views.createProject, name='create-project'),
]
