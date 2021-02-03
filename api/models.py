from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()
    author = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey("Post", related_name="post", on_delete=models.CASCADE, db_column="post")
    body = models.TextField()
    author = models.CharField(max_length=30)

    def  __str__(self):
        return self.author + " : " + self.body