from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from post.models import Post


class Subscription(models.Model):
    follower = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='rel_follower')
    followed = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='rel_followed')


class User(AbstractUser):
    token = models.CharField(max_length=10, blank=True, null=True)
    following = models.ManyToManyField('self', related_name='followers', symmetrical=False, blank=True,
                                       through=Subscription)
    latest_post_seen = models.DateTimeField(null=True, blank=True)

    def follow(self, user):
        self.following.add(user)
        self.save()

    def get_unseen_posts(self):
        if self.latest_post_seen:
            return Post.objects.filter(owner__in=self.following.all(), publish_datetime__gte=self.latest_post_seen)
        return Post.objects.filter(owner__in=self.following.all())

    def update_latest_post_seen(self):
        self.latest_post_seen = timezone.now()
        self.save()
