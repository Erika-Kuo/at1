from django.core import serializers
from django.shortcuts import render, redirect
from .models import Flashcard, SavedFlashcards
from django.contrib.auth.decorators import login_required
from .forms import FlashcardSaveForm

from .models import Flashcard

@login_required
def flashcards_view(request):
    print("Flashcards view function reached!")  # Add this print statement
    
    flashcards = Flashcard.objects.all()  # Retrieve all flashcards
    
    return render(request, 'eduprod/index.html', {'flashcards': flashcards})

@login_required
def saved_flashcards_view(request):
    if request.method == 'POST':
        form = FlashcardSaveForm(request.POST)
        if form.is_valid():
            flashcard_id = form.cleaned_data['flashcard_id']
            flashcard = Flashcard.objects.get(id=flashcard_id)
            saved_flashcard = SavedFlashcards.objects.create(user=request.user, flashcard=flashcard)
            saved_flashcard.save()
            return redirect('eduprod:saved_flashcards')
    else:
        form = FlashcardSaveForm()
    
    saved_flashcards = SavedFlashcards.objects.filter(user=request.user)
    context = {
        'saved_flashcards': saved_flashcards,
        'form': form,
    }
    return render(request, 'eduprod/saved_flashcards.html', context)

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



