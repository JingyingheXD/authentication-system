from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model
User = get_user_model()

class UserAccount(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=15)

     