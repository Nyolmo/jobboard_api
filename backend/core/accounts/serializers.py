from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.tokens import RefreshToken


User = get_user_model()

class User(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators = [validate_password]

    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )

    role = serializers.CharField(
        choices=ROLE_CHOICES, max_length=20, default=ROLE_FREELANCER
    )