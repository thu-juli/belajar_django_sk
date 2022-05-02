from django.contrib import admin
from .models import Post


class adminPost(admin.ModelAdmin):
    readonly_fields = ('slug',)


admin.site.register(Post, adminPost)
