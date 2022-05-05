from django.db import models


class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    username = models.CharField(max_length=100)
    hobby = models.CharField(max_length=100, blank=True)

    def __str__(self):
        fullname = str(self.first_name + ' ' + self.last_name)
        return fullname
