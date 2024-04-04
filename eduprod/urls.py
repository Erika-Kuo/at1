from django.urls import path
from . import views

app_name = 'eduprod'

urlpatterns = [
    path('', views.index, name='index'),
    path('flashcards/', views.flashcards_view, name='flashcards'),
    path('flashcards/next/', views.flashcards_view, name='next_flashcard'),
    path('save_flashcard/', views.saved_flashcards, name='save_flashcard'),
    path('saved_flashcards/', views.saved_flashcards, name='saved_flashcards'),
]