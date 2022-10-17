from rest_framework import routers

from post.views import PostViewSet

posts_router = routers.DefaultRouter()
posts_router.register(r'posts', PostViewSet)