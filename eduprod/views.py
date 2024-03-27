from django.db import models
from django.shortcuts import render, Http404
from django.views.generic import ListView, DetailView

from .models import Word

class IndexView(ListView):
    template_name = "hello/index.html"
    model = Word

class DetailView(DetailView):
    template_name = "hello/detail.html"
    model = Word

def index(request):
    words = Word.objects.all()
    if not words:
        raise Http404("No words found")
    context = {"words": words}
    return render(request, "hello/index.html", context)

def detail(request, pk):
    try:
        word = Word.objects.get(pk=pk)
    except Word.DoesNotExist:
        raise Http404("Word not found")
    context = {"word": word}
    return render(request, "hello/detail.html", context)