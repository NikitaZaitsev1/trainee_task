from django.urls import path, include

from page.routers.routers import pages_router, tags_router

urlpatterns = [
    path('api/v1/', include(pages_router.urls)),
    path('api/v1/', include(tags_router.urls)),
]
