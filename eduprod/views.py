from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FlashcardSaveForm
from .models import Flashcard, SavedFlashcards
from django.http import JsonResponse

@login_required
def flashcards_view(request):
    flashcards = Flashcard.objects.all()
    current_index = int(request.GET.get('current_index', 0))

    if current_index + 1 >= len(flashcards):
        current_index = 0
    else:
        current_index += 1

    flashcard = flashcards[current_index]

    context = {
        'flashcard': flashcard,
        'current_index': current_index
    }

    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        return JsonResponse({'context': context})
    else:
        return render(request, 'eduprod/index.html', context)

@login_required
def saved_flashcards(request):
    if request.method == 'POST':
        form = FlashcardSaveForm(request.POST)

        if form.is_valid():
            flashcard_id = form.cleaned_data['flashcard']
            flashcard = Flashcard.objects.get(id=flashcard_id)
            saved_flashcard = SavedFlashcards.objects.create(user=request.user, flashcard=flashcard)
            saved_flashcard.save()

            return JsonResponse({
                'saved': True
            })

    return JsonResponse({
        'saved': False
    })

@login_required
def index(request):
    flashcards = Flashcard.objects.order_by('?')[:5]
    saved_flashcards = SavedFlashcards.objects.filter(user=request.user)

    context = {
        'flashcards': flashcards,
        'saved_flashcards': saved_flashcards,
    }

    return render(request, 'eduprod/index.html', context)
