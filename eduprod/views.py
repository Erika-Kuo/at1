from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FlashcardSaveForm
from .models import Flashcard, SavedFlashcards

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

    flashcards = Flashcard.objects.all()  # Retrieve all flashcards
    saved_flashcards = SavedFlashcards.objects.filter(user=request.user)

    context = {
        'saved_flashcards': saved_flashcards,
        'form': form,
        'flashcards': flashcards,  # Pass flashcards to the template
    }

    return render(request, 'eduprod/saved_flashcards.html', context)

@login_required
def index(request):
    flashcards = Flashcard.objects.order_by('?')[:5]
    saved_flashcards = SavedFlashcards.objects.filter(user=request.user)

    context = {
        'flashcards': flashcards,
        'saved_flashcards': saved_flashcards,
    }

    return render(request, 'eduprod/index.html', context)

@login_required
def next_flashcard(request):
    flashcards = Flashcard.objects.all()
    current_index = int(request.GET.get('current_index', 0))

    if current_index + 1 >= len(flashcards):
        current_index = 0
    else:
        current_index += 1

    flashcard = flashcards[current_index]

    context = {
        'front': flashcard.front,
        'back': flashcard.back,
        'id': flashcard.id,
    }

    return render(request, 'eduprod/index.html', context)