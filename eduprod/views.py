from django.core import serializers
from django.shortcuts import render, redirect
from .models import Flashcard, SavedFlashcards
from django.contrib.auth.decorators import login_required

@login_required
def flashcards_view(request):
    flashcards = Flashcard.objects.order_by('?')[:5]
    flashcards_json = serializers.serialize('json', flashcards)
    return render(request, 'eduprod/flashcards.html', {'flashcards_json': flashcards_json})

@login_required
def saved_flashcards_view(request, flashcard_id):
    if flashcard_id:
        flashcard = Flashcard.objects.get(id=flashcard_id)
        saved_flashcards = SavedFlashcards(user=request.user, flashcard=flashcard)
        saved_flashcards.save()
    return redirect('eduprod:index')

@login_required
def index(request):
    flashcards = Flashcard.objects.order_by('?')[:5]
    saved_flashcards = SavedFlashcards.objects.filter(user=request.user)
    flashcard = flashcards.first()  # Assuming you want to pass the first flashcard in the context

    context = {
        'flashcards': flashcards,
        'saved_flashcards': saved_flashcards,
        'flashcard': flashcard,  # Include the flashcard object in the context
    }

    return render(request, 'eduprod/index.html', context)


