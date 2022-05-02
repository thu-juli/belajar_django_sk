from django.db import models
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    category = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(blank=True, editable=False)
    created = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
