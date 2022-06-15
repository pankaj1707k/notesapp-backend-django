from rest_framework.generics import DestroyAPIView, ListCreateAPIView

from .models import Notebook
from .serializers import NotebookSerializer


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
