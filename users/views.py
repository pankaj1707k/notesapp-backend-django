from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from .serializers import UserCreateSerializer

User = get_user_model()


class CreateUser(CreateAPIView):
    """
    Concrete view to create a User instance
    """

    permission_classes = [AllowAny]
    serializer_class = UserCreateSerializer
