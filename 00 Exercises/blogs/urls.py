from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:categoryInput>/', views.category, name='category'),
    path('post/<slug:slugIput>/', views.singlePost, name='single-post')
]
