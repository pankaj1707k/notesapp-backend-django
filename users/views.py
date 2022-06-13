from django.contrib.auth import get_user_model, logout
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.views import APIView

from .serializers import UserCreateSerializer

User = get_user_model()


class CreateUser(CreateAPIView):
    """
    Concrete view to create a User instance
    """

    permission_classes = [AllowAny]
    serializer_class = UserCreateSerializer


class LogoutUser(APIView):
    """
    Concrete view to logout a user.
    """

    def get(self, request):
        """
        Method to handle logout request.
        Deletes the auth_token of the user.
        """
        user = request.user
        user.auth_token.delete()
        logout(request)
        message = {"success": "user logged out"}
        return Response(message, HTTP_200_OK)


class DeleteUser(APIView):
    """
    Concrete view to delete an existing User instance
    """

    def delete(self, request):
        instance = request.user
        instance.delete()
        return Response(status=HTTP_204_NO_CONTENT)
