from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
