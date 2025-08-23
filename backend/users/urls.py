from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import AuthViewSet

router = SimpleRouter()
router.register(r'auth', AuthViewSet, basename='auth')

urlpatterns = [
    path('', include(router.urls))
]