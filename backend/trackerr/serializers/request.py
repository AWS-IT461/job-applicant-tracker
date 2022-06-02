from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from backend.trackerr import models


class LoginRequestSerializer(TokenObtainPairSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if email and password:
            if not (user := authenticate(email=email, password=password)):
                raise serializers.ValidationError("Email or password is incorrect")
        else:
            raise serializers.ValidationError("Email or password is required")

        attrs['user'] = user
        return attrs
