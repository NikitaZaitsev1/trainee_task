from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from post.models import Post
from post.serializers.serializers import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
