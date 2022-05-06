from django.urls import path
from .views import ArticleListView


app_name = 'article'
urlpatterns = [
    path('', ArticleListView.as_view(), name='list')
]
