from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import (
    CreateUser,
    DeleteUser,
    LogoutUser,
    RetrieveUser,
    UpdatePassword,
    UpdateUser,
)

urlpatterns = [
    path("register/", CreateUser.as_view()),
    path("login/", obtain_auth_token),
    path("logout/", LogoutUser.as_view()),
    path("delete/", DeleteUser.as_view()),
    path("retrieve/", RetrieveUser.as_view()),
    path("update/", UpdateUser.as_view()),
    path("update/password/", UpdatePassword.as_view()),
]
