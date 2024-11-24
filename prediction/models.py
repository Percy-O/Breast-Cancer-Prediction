from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    # username = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    
    def __unicode__(self):
        
        return f'{self.username}'