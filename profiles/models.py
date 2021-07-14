from django.db import models
from django.contrib.auth.models import User

# Create your models here.

"""
OneToOneField - Since, each user can work on only one profile.

class models.User
The Django’s built-in authentication system is great. For the most part we can use it out-of-the-box, saving a lot of development and testing effort. It fits most of the use cases and is very safe.

User objects have the following fields:
    username, first_name, last_name, email, password, groups, user_permissions, etc.

The class also has several methods and manager methods for ease-of-use.

on_delete = models.CASCADE ensures that on deleting a user, the profile gets deleted.

"""


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='No Bio')
    avatar = models.ImageField(upload_to='avatars', default='no_picture.png')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Profile of {self.user.username}"
