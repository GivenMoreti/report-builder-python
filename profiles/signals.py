#automatically creates a profile when user is added 1st step

from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

#by just adding user a profile is automatically created
@receiver(post_save,sender =User)
def post_save_create_profile(sender,instance,created,**kwargs):
    if created:
        #the profile is only created once 
        Profile.objects.create(user=instance)

