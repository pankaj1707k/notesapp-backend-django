from rest_framework.generics import (
    DestroyAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.response import Response
from rest_framework.status import *

from .models import Note, Notebook
from .serializers import NotebookSerializer, NoteSerializer


class ListCreateNotebook(ListCreateAPIView):
    """
    View to list and create Notebook instance.
    List all Notebook instances of authenticated user.
    """

    serializer_class = NotebookSerializer

    def get_queryset(self):
        return Notebook.objects.filter(user=self.request.user)


class DeleteNotebook(DestroyAPIView):
    """
    View to delete a Notebook instance
    """

    serializer_class = NotebookSerializer

    def get_queryset(self):
        return Notebook.objects.filter(user=self.request.user)


class ListCreateNote(ListCreateAPIView):
    """
    View to create and list Note instances.
    List all notes for given notebook id.
    """

    serializer_class = NoteSerializer

    def get_queryset(self):
        return Note.objects.filter(notebook__user=self.request.user)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(notebook__id=kwargs.get("nb"))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        notebook_queryset = Notebook.objects.filter(user=request.user)
        try:
            notebook_queryset.get(pk=kwargs.get("nb"))
        except Notebook.DoesNotExist:
            msg = {"detail": "notebook not found"}
            return Response(msg, HTTP_404_NOT_FOUND)
        if int(request.data.get("notebook")) != kwargs.get("nb"):
            msg = {"detail": "notebook id mismatch in url and request body"}
            return Response(msg, HTTP_400_BAD_REQUEST)
        return self.create(request, *args, **kwargs)


class GetUpdateDeleteNote(RetrieveUpdateDestroyAPIView):
    """
    View to perform get, update and delete operations on a single Note instance
    """

    serializer_class = NoteSerializer

    def get_queryset(self):
        return Note.objects.filter(notebook__user=self.request.user)
