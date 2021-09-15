from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Post
from user.models import User
from rest_framework.response import Response


class PublishPost(APIView):

    def post(self, request, *args, **kwargs):
        token = request.data.get('Token', '')
        text = request.data.get('text', '')
        user = get_object_or_404(User, token=token)
        Post.objects.create(text=text, owner=user)
        return Response(data={"status": "OK"})
# Create your views here.
