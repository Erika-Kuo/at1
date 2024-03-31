from django.urls import path
from . import views

app_name = 'eduprod'

urlpatterns = [
    path('', views.index, name='index'),
    path('flashcards/', views.flashcards_view, name='flashcards'),
    path('saved_flashcards/<int:flashcard_id>/', views.saved_flashcards_view, name='saved_flashcards'),
]

