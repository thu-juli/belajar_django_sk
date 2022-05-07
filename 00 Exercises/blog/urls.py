from django.urls import path
from .views import (
    BlogListView,
    DeleteListView,
    FromListView,
)


app_name = 'blog'
urlpatterns = [
    path('delete/<int:deleteId>/', DeleteListView.as_view(), name='delete-view'),
    path('update/<slug:slug>/',
         FromListView.as_view(mode='update'), name='update-view'),
    path('create/', FromListView.as_view(), name='create-view'),
    path('', BlogListView.as_view(), name='list-view'),
]
