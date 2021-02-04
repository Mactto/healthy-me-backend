from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()
    author = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Comment(models.Model):
    body = models.TextField()
    author = models.CharField(max_length=30)
    post_id = models.CharField(max_length=5, default='')

    def  __str__(self):
        return self.author + " : " + self.body