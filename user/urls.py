from django.urls import path, include

from user.routers.routers import users_router

urlpatterns = [
    path('api/v1/', include(users_router.urls)),
]
