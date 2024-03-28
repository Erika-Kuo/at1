from django import forms
from django.contrib import admin
from .models import VocabularyWord

# Register VocabularyWord model with the default ModelAdmin
admin.site.register(VocabularyWord)