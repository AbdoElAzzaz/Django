from django.db import models


# Create your models here.
class tasks(models.Model):
    task_name = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    stat = models.IntegerField(default=0)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.task_name
