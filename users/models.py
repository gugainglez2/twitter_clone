from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    bio = models.TextField(max_length=160, blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', default='default.png', blank=True)
    
    # ManyToMany self-referencial para o sistema de seguir
    following = models.ManyToManyField(
        "self", 
        symmetrical=False, 
        related_name="followers", 
        blank=True
    )

    def __str__(self):
        return self.username