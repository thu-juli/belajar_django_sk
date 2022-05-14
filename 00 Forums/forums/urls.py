from django.urls import path
from .views import ForumList, ForumCreate, ForumDetail, ForumUpdate, ForumDelete, CommentCreate

app_name = 'forums'
urlpatterns = [
    path('comment/create/<int:pk>', CommentCreate.as_view(), name='comment-create'),
    path('create/', ForumCreate.as_view(), name='create'),
    path('delete/<int:pk>/', ForumDelete.as_view(), name='delete'),
    path('update/<int:pk>/', ForumUpdate.as_view(), name='update'),
    path('detail/<slug:slug>/', ForumDetail.as_view(), name='detail'),
    path('', ForumList.as_view(), name='list'),
]
