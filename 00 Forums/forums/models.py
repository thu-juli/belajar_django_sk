from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.shortcuts import reverse
from random import randint
# Create your models here.


class Forum(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('forums:detail', kwargs={'slug': self.slug})

    def save(self):
        if self.pk == None:
            extra = str(randint(1, 10000))
            self.slug = slugify(self.title) + '-' + extra
        super().save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('forums:list')
