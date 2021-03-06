from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 'email', 'token'
        )


class PostUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
        )
