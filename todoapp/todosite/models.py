from django.db import models

from django.utils import timezone


class Todo(models.Model):
    title = models.CharField(max_length=50)
    details = models.TextField(max_length=500)
    date = models.DateField()


    def __str__(self):
        return self.title