from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class FromModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    body = models.TextField()
    subject = models.ManyToManyField(Category, blank=True)
    date_birth = models.DateField()

    def __str__(self):
        return self.name
