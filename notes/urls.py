from django.urls import path

from .views import DeleteNotebook, ListCreateNotebook

urlpatterns = [
    path("notebooks/", ListCreateNotebook.as_view()),
    path("notebooks/<pk>/", DeleteNotebook.as_view()),
]
