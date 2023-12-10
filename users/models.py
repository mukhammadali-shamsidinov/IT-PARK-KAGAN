from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    user_img = models.ImageField(default='h.jpg',upload_to='users/')
    bio = models.TextField()
