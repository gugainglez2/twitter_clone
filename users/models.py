from django.contrib.auth.models import AbstractUser
from django.db import models
from cloudinary.models import CloudinaryField

class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = CloudinaryField('image', blank=True, null=True)
    
    following = models.ManyToManyField(
        "self", 
        symmetrical=False, 
        related_name="followers", 
        blank=True
    )

    def __str__(self):
        return self.username
    
    following = models.ManyToManyField(
        "self", 
        symmetrical=False, 
        related_name="followers", 
        blank=True
    )

    def __str__(self):
        return self.username