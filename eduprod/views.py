from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import VocabularyWord

class IndexView(ListView):
    template_name = "hello/index.html"
    model = VocabularyWord

class DetailView(DetailView):
    template_name = "hello/detail.html"
    model = VocabularyWord