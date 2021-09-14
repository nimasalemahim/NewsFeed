from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    token = models.CharField(max_length=10)
    followers = models.ManyToManyField('self', related_name='users_followed')
# Create your models here.
