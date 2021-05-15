from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    body = models.TextField()  # What the user tipes in on the post 
    created_on = models.DateTimeField(default=timezone.now)  # when the user post, its the the exact time
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # find the current user that creates the post


class Comment(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(default=timezone.now) # when the user post, its the the exact time
    auther = models.ForeignKey(User, on_delete=models.CASCADE)  # find the current user that creates the post
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
