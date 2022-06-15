from rest_framework import serializers

from .models import Note, Notebook


class NotebookSerializer(serializers.ModelSerializer):
    """
    Serializer to handle Notebook instances
    """

    class Meta:
        model = Notebook
        fields = "__all__"
        extra_kwargs = {"user": {"required": False}}

    def validate(self, attrs):
        user = self.context["request"].user
        attrs["user"] = user
        queryset = Notebook.objects.filter(name=attrs["name"], user=user)
        if queryset.exists():  # Check if (name, user) is unique
            msg = {"uniqueness failed": "name per user must be unique"}
            raise serializers.ValidationError(detail=msg, code=400)
        return attrs


class NoteSerializer(serializers.ModelSerializer):
    """
    Serializer to handle Note instances
    """

    class Meta:
        model = Note
        fields = "__all__"
