from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from post.models import Post
from post.permissions.post_user_permission import PostUserPermission
from post.serializers.serializers import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = (IsAuthenticatedOrReadOnly,)
        else:
            self.permission_classes = (PostUserPermission,)
        return super(PostViewSet, self).get_permissions()
