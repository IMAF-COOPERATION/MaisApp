from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=20, blank=True)
    photo = models.ImageField(upload_to='profils/', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # tu peux aussi mettre [] si tu veux utiliser uniquement email

    def __str__(self):
        return self.email
