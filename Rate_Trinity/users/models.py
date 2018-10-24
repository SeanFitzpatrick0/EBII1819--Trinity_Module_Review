from django.db import models
from django.contrib.auth.models import User
from modules.models import Module

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    modules = models.ManyToManyField(Module)

    def __str__(self):
        return f'{self.user} Profile'