from django.contrib.auth.models import User
from django.db import models

# Create your models here.

##Goal is to add on to user class
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) ##this tells Django what to do to a Profile row if its linked User gets deleted.
    bio = models.TextField(blank=True)
    