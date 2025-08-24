from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.urls import urlpatterns
from .views import EventViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet, basename='event')

url_patterns = [
    path('',include(router.urls))
]