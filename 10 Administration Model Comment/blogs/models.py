from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    creat_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    blogs = models.ForeignKey(Blog, on_delete=callable)
    comments = models.TextField()
    creat_at = models.DateTimeField(auto_now_add=True)
