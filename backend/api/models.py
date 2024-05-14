from django.db import models

# Create your models here.
class Todo(models.Model):

    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=10)


    def __str__(self):
        return self.username