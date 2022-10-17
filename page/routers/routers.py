from rest_framework import routers

from page.views import PageViewSet, TagViewSet

pages_router = routers.DefaultRouter()
tags_router = routers.DefaultRouter()
pages_router.register(r'pages', PageViewSet)
tags_router.register(r'tags', TagViewSet)
