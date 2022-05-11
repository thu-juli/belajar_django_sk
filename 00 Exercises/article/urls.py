from django.urls import path
from .views import indexArticleView, AddArticleView

app_name = 'article'
urlpatterns = [
    path('add/', AddArticleView, name='add'),
    path('', indexArticleView, name='home'),
]
