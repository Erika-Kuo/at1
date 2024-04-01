from django.urls import path
from . import views

app_name = 'eduprod'

urlpatterns = [
    path('', views.index, name='index'),
    path('flashcards/', views.flashcards_view, name='flashcards'),
    path('flashcards/next/', views.next_flashcard, name='next_flashcard'),
    path('saved_flashcards/', views.saved_flashcards_view, name='saved_flashcards'),
    path('saved_flashcards/', views.saved_flashcards_view, name='saved_flashcards'),
]