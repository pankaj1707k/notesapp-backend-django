from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import *

from .serializers import UserCreateSerializer

User = get_user_model()


class CreateUser(CreateAPIView):
    """
    Concrete view to create a User instance
    """

    permission_classes = [AllowAny]
    serializer_class = UserCreateSerializer

    def create(self, request, *args, **kwargs):
        """
        Method to create a User instance.
        Overridden to generate custom response.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Send token of the new user in response along with other data
        user_data = dict(serializer.data)
        token = Token.objects.get(user__username=user_data["username"]).key
        user_data["token"] = token
        return Response(user_data, HTTP_201_CREATED)
