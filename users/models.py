from distutils.command.upload import upload
from email.policy import default

from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete = models.CASCADE)
    image = models.ImageField(default='drake.jpg', upload_to='profile_pics' ) 


    def __str__ (self):
        #return self.image

        return f'{self.user.username} Profile'



