from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    path('form/', views.index, name='index'),
    path('model/', views.forms, name='model'),
    path('', views.home, name='home'),
]
