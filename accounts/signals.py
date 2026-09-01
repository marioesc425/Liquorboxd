from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


##Django signals let one part of the app "announce" an event (a User was saved), and other code can react to it — without User needing to know Profile exists
##We want the post_save signal on User, which fires every time a User is saved (created or updated)
##The if created: check matters — it ensures we only create a Profile on the first save (new user), not every time an existing user's info changes
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
##Note: The @receiver decorator is a shortcut for connecting the signal to the function. It registers create_profile as a listener for the post_save signal on the User model.      