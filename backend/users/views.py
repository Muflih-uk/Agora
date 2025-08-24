# Create your views here.
from wsgiref.validate import validator

from django.core.serializers import serialize
from django.urls.converters import REGISTERED_CONVERTERS
from rest_framework import viewsets, status
from rest_framework.decorators import action, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from .models import AppUser
from .serializers import AppUserLoginSerializer, AppUserSignUpSerializer

class AuthViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['post'], permission_classes = [AllowAny])
    def register(self, request):
        serializer = AppUserSignUpSerializer(data= request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                "user": AppUserSignUpSerializer(user).data,
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], permission_classes = [AllowAny])
    def login(self, request):
        serializer = AppUserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]
        refresh = RefreshToken.for_user(user)

        return Response({
            "user": AppUserSignUpSerializer(user).data,
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], permission_classes = [IsAuthenticated])
    def logout(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)
        except Exception:
            return Response({"detail": "Invalid refresh token."}, status=status.HTTP_400_BAD_REQUEST)