from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import VocabularyWord
import logging

logger = logging.getLogger(__name__)

class IndexView(ListView):
    template_name = "hello/index.html"
    model = VocabularyWord

    def get(self, request, *args, **kwargs):
        logger.info("Starting to render the index page...")
        response = super().get(request, *args, **kwargs)
        logger.info("Finished rendering the index page.")
        return response

class DetailView(DetailView):
    template_name = "hello/detail.html"
    model = VocabularyWord

    def get(self, request, *args, **kwargs):
        logger.info("Starting to render the detail page...")
        response = super().get(request, *args, **kwargs)
        logger.info("Finished rendering the detail page.")
        return response
    
    