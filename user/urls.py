from django.urls import path, include

from user.routers.routers import users_router

urlpatterns = [
    path('api/v1/', include(users_router.urls)),
    path('api/v1/auth/', include('rest_framework.urls')),
]
