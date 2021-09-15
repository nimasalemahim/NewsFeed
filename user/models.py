from django.db import models
from django.contrib.auth.models import AbstractUser


class Subscription(models.Model):
    follower = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='rel_follower')
    followed = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='rel_followed')


class User(AbstractUser):
    token = models.CharField(max_length=10, blank=True, null=True)
    following = models.ManyToManyField('self', related_name='followers', symmetrical=False, blank=True,
                                       through=Subscription)

    def follow(self, user):
        self.following.add(user)
        self.save()
# Create your models here.
