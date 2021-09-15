from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import User
from rest_framework.response import Response


class SubscribeViewSet(APIView):

    def post(self, request, *args, **kwargs):
        token = request.data.get('Token', '')
        email = request.data.get('email', '')
        this_user = get_object_or_404(User, token=token)
        user_to_follow = get_object_or_404(User, email=email)
        this_user.follow(user_to_follow)
        return Response(data={'status': 'OK'})
