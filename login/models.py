from django.db import models


# Create your models here.
class users(models.Model):
    username = models.CharField(max_length=200)
    pwd = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.username