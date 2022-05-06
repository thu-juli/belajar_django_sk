from django.db import models
from django.utils.text import slugify


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    slug = models.SlugField(blank=True, editable=False)

    def __str__(self):
        return self.title

    def save(self):
        self.slug = slugify(self.title)
        super(Article, self).save()
