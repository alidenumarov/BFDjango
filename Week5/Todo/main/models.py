from django.db import models

# Create your models here.

class Todo(models.Model):
    task = models.CharField(max_length=500)
    created = models.DateTimeField()
    due_on = models.DateTimeField()
    owner = models.CharField(max_length=100)
    mark = models.BooleanField()

    def __str__(self):
        return self.task