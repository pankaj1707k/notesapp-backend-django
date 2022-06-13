from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import CreateUser, LogoutUser

urlpatterns = [
    path("register/", CreateUser.as_view()),
    path("login/", obtain_auth_token),
    path("logout/", LogoutUser.as_view()),
]
