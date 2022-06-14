from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Notebook(models.Model):
    """
    Model to represent a group of notes
    """

    name = models.CharField(_("name"), max_length=20)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="notebooks",
        related_query_name="notebook",
    )

    def __str__(self) -> str:
        return self.name


class Note(models.Model):
    """
    Model to represent a Note
    """

    content = models.TextField(_("content"))
    notebook = models.ForeignKey(
        Notebook,
        on_delete=models.CASCADE,
        related_name="notes",
        related_query_name="note",
    )
    updated_on = models.DateTimeField(_("updated on"), auto_now=True)

    def __str__(self) -> str:
        return self.content[:50] + "..."

    class Meta:
        ordering = ["-updated_on"]
