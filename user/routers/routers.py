from rest_framework import routers

from user.views import UserViewSet

users_router = routers.DefaultRouter()
users_router.register(r'users', UserViewSet)