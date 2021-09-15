from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Post
from user.models import User
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .serializers import PostSerializer


class PublishPost(APIView):

    def post(self, request, *args, **kwargs):
        token = request.data.get('Token', '')
        text = request.data.get('text', '')
        user = get_object_or_404(User, token=token)
        Post.objects.create(text=text, owner=user)
        return Response(data={"status": "OK"})


class GetPosts(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        token = self.request.query_params.get('token', '')
        user = get_object_or_404(User, token=token)
        posts = user.get_unseen_posts()
        user.update_latest_post_seen()
        return posts
