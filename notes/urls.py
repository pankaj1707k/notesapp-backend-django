from django.urls import path

from .views import DeleteNotebook, ListCreateNote, ListCreateNotebook

urlpatterns = [
    path("notebooks/", ListCreateNotebook.as_view()),
    path("notebooks/<pk>/", DeleteNotebook.as_view()),
    path("notebooks/<int:nb>/notes/", ListCreateNote.as_view()),
]
