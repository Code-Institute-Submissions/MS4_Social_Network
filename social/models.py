from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Post model
class Post(models.Model):
    body = models.TextField()  # What the user tipes in on the post 
    created_on = models.DateTimeField(default=timezone.now)  # when the user post, its the the exact time
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # find the current user that creates the post


# Comment model
class Comment(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(default=timezone.now) # when the user post, its the the exact time
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # find the current user that creates the post
    post = models.ForeignKey('Post', on_delete=models.CASCADE)


# Profile model ( One user profile per user, on_delete= delete all)
class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True, null=True) # Blank = you dont need to enter something in your profile, null = its allowed to be empty in DB
    bio = models.TextField(max_length=500, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    picture = models.ImageField(upload_to='uploads/profile_pictures', default='uploads/profile_pictures/default.png', blank=True)
