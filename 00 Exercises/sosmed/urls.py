from django.urls import path
from .views import ListView, DetailView, DeleteView, FormView

app_name = 'sosmed'
urlpatterns = [
    path('detail/<str:id>/', DetailView.as_view(), name='detail-view'),
    path('delete/<str:id>/', DeleteView.as_view(), name='delete-view'),
    path('create/', FormView.as_view(), name='create-view'),
    path('update/<str:id>/', FormView.as_view(mode='update'), name='update-view'),
    path('', ListView.as_view(), name='list-view'),
]
