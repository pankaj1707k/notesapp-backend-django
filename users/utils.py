""" Utility functions """


def get_image_path(instance, filename) -> str:
    """Rename file and get upload path"""
    ext = filename.split(".")[-1]  # extract file extension
    return f"avatars/{instance.user.username}_avatar.{ext}"
