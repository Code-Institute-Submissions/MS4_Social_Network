from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Post model
class Post(models.Model):
    body = models.TextField()  # What the user tipes in on the post
    image = models.ImageField(upload_to='uploads/post_photos', blank=True, null=True) 
    created_on = models.DateTimeField(default=timezone.now)  # when the user post, its the the exact time
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # find the current user that creates the post
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')


# Comment model
class Comment(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)  # when the user post, its the the exact time
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # find the current user that creates the post
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True, related_name='comment_likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='comment_dislikes')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='+')

    @property  # Decorator to make it more easely to access this function
    def children(self):
        return Comment.objects.filter(parent=self).order_by('-created_on').all()

    @property  # check if is parent
    def is_parent(self):
        if self.parent is None:
            return True
        return False


# Profile model ( One user profile per user, on_delete= delete all)
class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True, null=True) # Blank = you dont need to enter something in your profile, null = its allowed to be empty in DB
    bio = models.TextField(max_length=500, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    picture = models.ImageField(upload_to='uploads/profile_pictures', default='uploads/profile_pictures/default.png', blank=True)
    followers = models.ManyToManyField(User, blank=True, related_name='followers')


# Create user profile
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


# Save user profile
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
