from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Profile

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    """
    Serializer to handle creation of User instance
    """

    token = serializers.CharField(source="auth_token.key", read_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "token"]
        extra_kwargs = {
            "email": {"validators": [UniqueValidator(User.objects.all())]},
            "password": {"write_only": True},
        }

    def validate(self, attrs):
        """
        Validate POST data during deserialization
        """

        # Run django's default password validators
        validate_password(attrs["password"])

        return super().validate(attrs)


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer to handle profile instances of users
    """

    class Meta:
        model = Profile
        fields = ["phone", "avatar"]


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer to retrieve and update User information
    including data from related Profile instance.
    """

    profile = ProfileSerializer(required=False)

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "profile"]
        extra_kwargs = {"email": {"validators": [UniqueValidator(User.objects.all())]}}

    def update(self, instance, validated_data):
        # Update auth data
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.save()

        # Update profile data
        profile_data = validated_data.get("profile", {})
        profile = instance.profile
        profile.phone = profile_data.get("phone", profile.phone)
        profile.avatar = profile_data.get("avatar", profile.avatar)
        profile.save()

        return instance
