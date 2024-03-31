from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Flashcard

@login_required(login_url='users:login')  # Specify your login URL
def flashcards_view(request):
    flashcards = Flashcard.objects.all()
    return render(request, 'flashcards/flashcards.html', {'flashcards': flashcards})