from django.urls import path, include

from post.routers.routers import posts_router, comments_router

urlpatterns = [
    path('api/v1/', include(posts_router.urls)),
    path('api/v1/', include(comments_router.urls)),
]
