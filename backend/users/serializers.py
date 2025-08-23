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

class AppUserLoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token