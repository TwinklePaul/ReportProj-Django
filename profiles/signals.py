from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

"""
Signals is sort of a communication system between the models.

One model = sender
and sender sends a notification about an action that occur
Based on that information, the receiver performs different actions.

Here, sender = user, receiver = profile. 

User will inform the profile that a user instance has been created.
Based on that, the profile of the user will be created.


@receiver()
def post_save_create_profile 
is same as saying:
post_save_create_profile = receiver(post_save_create_profile)

With the receiver decorator, we specify that the signal is going to be post-save and sender is going to be the User.
below we add the funtionality.

the created argument will only be true once.
Only when the instance of the sender(User) is created, the created argument will be true.

In profile object, we are setting the user field as the instance of the Sender(User) object.

Next, goto apps.py, override the ready method and bring in signals.

"""


@receiver(post_save, sender=User)
def post_save_create_profile(sender, instance, created, **kwargs):
    print(sender)
    print(instance)
    print(created)

    if created:
        Profile.objects.create(user=instance)
