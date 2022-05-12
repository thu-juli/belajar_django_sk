from django.contrib import admin
from .models import Forum, Comment

# Register your models here.


class AdminForum(admin.ModelAdmin):
    readonly_fields = (
        'slug',
        'created'
    )


admin.site.register(Forum, AdminForum)
admin.site.register(Comment)
