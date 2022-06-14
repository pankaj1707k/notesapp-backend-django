from django.urls import path

from .views import ListCreateNotebook

urlpatterns = [path("notebooks/", ListCreateNotebook.as_view())]
