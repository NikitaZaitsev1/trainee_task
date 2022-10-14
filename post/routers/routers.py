from rest_framework import routers

from post.views import PostViewSet

posts_router = routers.SimpleRouter()
posts_router.register(r'posts', PostViewSet)