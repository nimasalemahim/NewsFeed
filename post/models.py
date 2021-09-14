from django.db import models


class Post(models.Model):
    text = models.TextField()
    published = models.BooleanField(default=False)
    owner = models.ForeignKey('user.User', related_name='posts', on_delete=models.CASCADE)
# Create your models here.
