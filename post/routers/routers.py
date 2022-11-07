from rest_framework import routers

from post.views import PostViewSet, CommentViewSet, LikeViewSet

posts_router = routers.DefaultRouter()
comments_router = routers.DefaultRouter()
likes_router = routers.DefaultRouter()

posts_router.register(r'posts', PostViewSet)
comments_router.register(r'comments', CommentViewSet)
likes_router.register(r'likes', LikeViewSet)
