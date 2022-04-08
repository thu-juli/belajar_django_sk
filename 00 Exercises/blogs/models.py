from django.db import models
import uuid


class Project(models.Model):
    title = models.CharField(max_length=254)
    featured_image = models.ImageField(
        null=True, blank=True, default='default.jpg')
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title


class Review(models.Model):
    VOTE_TYPE = [
        ('up', 'up vote'),
        ('down', 'down  vote'),
    ]
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(blank=True, null=True)
    value = models.CharField(max_length=254, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.value
