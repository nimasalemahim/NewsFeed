from django.db import models
from django.utils import timezone


class Post(models.Model):
    text = models.TextField()
    publish_datetime = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey('user.User', related_name='posts', on_delete=models.CASCADE)

# Create your models here.
