from rest_framework import routers

from user.views import UserViewSet

users_router = routers.SimpleRouter()
users_router.register(r'users', UserViewSet)