from django.db import models
from django.contrib.auth.models import User

class VocabularyWord(models.Model):
    word = models.CharField(max_length=255)
    definition = models.TextField()
    usage = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.word

class Flashcard(models.Model):
    word = models.ForeignKey(VocabularyWord, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    answer_revealed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.word.word} for user {self.user}"
    

class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username