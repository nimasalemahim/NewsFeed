from rest_framework import serializers
from user.models import User
import string
import random


def _generate_random_token():
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    while User.objects.filter(token=ran).exists():
        ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    return ran


class SignUpSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate(self, attrs):
        email = attrs.get('email')
        username = str(email).split('@')[0]
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('User Exists.')
        token = _generate_random_token()
        user = User.objects.create(username=username, email=email, password=token, token=token)
        attrs['user'] = user
        return attrs
