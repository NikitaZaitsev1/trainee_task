from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from innotter.enum_classes import Method, Action
from innotter.producer import publish
from innotter.pydantic_models import Stats
from post.models import Post, Comment, Like
from post.permissions.comment_permissions import CommentUserPermission
from post.permissions.post_user_permission import PostUserPermission
from post.serializers.comment_serializer import CommentSerializer
from post.serializers.like_serializer import LikeSerializer

from post.serializers.post_serializer import PostSerializer
from post.serializers.post_serializer_get import PostSerializerGet
from post.serializers.post_serializer_update import PostSerializerUpdate


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action == Method.LIST:
            return PostSerializerGet
        if self.action == Method.UPDATE or self.action == Method.PARTIAL_UPDATE:
            return PostSerializerUpdate
        return PostSerializer

    def get_permissions(self):
        if self.request.method == Method.GET:
            self.permission_classes = (IsAuthenticatedOrReadOnly,)
        else:
            self.permission_classes = (PostUserPermission,)
        return super(PostViewSet, self).get_permissions()

    def perform_create(self, serializer):
        stats = Stats(user_id=self.request.user.uuid, action=Action.CREATE_POST)
        publish(stats.json())
        serializer.save(owner=self.request.user)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.request.method == Method.GET:
            self.permission_classes = (IsAuthenticatedOrReadOnly,)
        else:
            self.permission_classes = (CommentUserPermission,)
        return super(CommentViewSet, self).get_permissions()


class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def perform_create(self, serializer):
        stats = Stats(user_id=self.request.user.uuid, action=Action.CREATE_LIKE)
        publish(stats.json())
        serializer.save(like_user=self.request.user)
