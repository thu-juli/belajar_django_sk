from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('contacts/', include('contacts.urls', namespace='contacts')),
    path('admin/', admin.site.urls),
]
