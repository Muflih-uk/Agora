from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import AppUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class AppUserSignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required= True, style= {'input_type': 'password'})

    class Meta:
        model = AppUser
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = AppUser.objects.create_user(
            username= validated_data["username"],
            email= validated_data['email'],
            password= validated_data['password']
        )

        return user

class AppUserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        user = authenticate(username=email, password=password)
        if not user:
            raise serializers.ValidationError({"detail": "Invalid email or password"})

        data["user"] = user
        return data
