from django.contrib.auth import get_user_model, logout
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.views import APIView

from .serializers import UpdatePasswordSerializer, UserCreateSerializer, UserSerializer

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


class RetrieveUser(RetrieveAPIView):
    """
    Concrete view to retrieve a User instance
    """

    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class UpdateUser(UpdateAPIView):
    """
    Concrete view to update a User instance
    including related Profile instance
    """

    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class UpdatePassword(UpdateAPIView):
    """
    Concrete view to update the password of a User instance
    """

    serializer_class = UpdatePasswordSerializer

    def update(self, request, *args, **kwargs):
        instance = self.request.user
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        msg = {"success": "password updated"}
        return Response(msg, HTTP_200_OK)
