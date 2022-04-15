from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.posts, name='posts'),
    path('<str:pk>/', views.singlePost, name='single-post'),
    path('create-post', views.createPost, name='create-post'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
