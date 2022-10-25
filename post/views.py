from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from innotter.enum_classes import Method
from post.models import Post
from post.permissions.post_user_permission import PostUserPermission
from post.serializers.post_serializer import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.request.method == Method.get:
            self.permission_classes = (IsAuthenticatedOrReadOnly,)
        else:
            self.permission_classes = (PostUserPermission,)
        return super(PostViewSet, self).get_permissions()
