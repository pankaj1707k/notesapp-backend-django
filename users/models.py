from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from .utils import get_image_path


class Profile(models.Model):
    """
    Model to represent the profile of a user.
    It holds the non-authentication related additional data of a user.
    It has a one-to-one relationship with the User model.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(_("phone number"), max_length=16, blank=True)
    avatar = models.ImageField(
        _("avatar"), default="avatars/default.png", upload_to=get_image_path
    )

    def __str__(self):
        return f"{self.user.username} profile"
