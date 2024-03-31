from django import forms
from .models import Flashcard

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ['question_text', 'answer_text']