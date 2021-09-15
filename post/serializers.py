from rest_framework import serializers
from .models import Post
from user.serializers import PostUserSerializer


class PostSerializer(serializers.ModelSerializer):
    owner = PostUserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('text', 'publish_datetime', 'owner')
