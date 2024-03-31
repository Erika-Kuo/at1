from django import forms
from .models import Flashcard

class FlashcardSaveForm(forms.Form):
    flashcard = forms.ModelChoiceField(queryset=Flashcard.objects.all(), empty_label=None)