from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

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