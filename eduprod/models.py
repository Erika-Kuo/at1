from django.db import models
from django.conf import settings

class Flashcard(models.Model):
    front = models.CharField(max_length=200)
    back = models.TextField()

    def __str__(self):
        return self.front
    
class SavedFlashcards(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    flashcard = models.ForeignKey(Flashcard, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.flashcard.front