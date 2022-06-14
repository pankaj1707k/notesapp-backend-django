from django.contrib import admin

from .models import Note, Notebook

admin.site.register(Notebook)
admin.site.register(Note)
