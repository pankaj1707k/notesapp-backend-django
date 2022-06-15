from django.urls import path

from .views import (
    DeleteNotebook,
    GetUpdateDeleteNote,
    ListCreateNote,
    ListCreateNotebook,
)

urlpatterns = [
    path("notebooks/", ListCreateNotebook.as_view()),
    path("notebooks/<pk>/", DeleteNotebook.as_view()),
    path("notebooks/<int:nb>/notes/", ListCreateNote.as_view()),
    path("notebooks/notes/<int:pk>/", GetUpdateDeleteNote.as_view()),
]
