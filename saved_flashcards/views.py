from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def saved_flashcards_view(request):
    # Logic for handling the saved flashcards functionality
    return render(request, 'saved_flashcards/saved_flashcards.html')