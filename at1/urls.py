from django.contrib import admin
from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt
from eduprod.views import index, flashcards_view, saved_flashcards_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('eduprod/', include(('eduprod.urls', 'eduprod'), namespace='eduprod')),
    path('accounts/login/', include('users.urls')),
    path('', csrf_exempt(index), name='index'),
    path('flashcards/', flashcards_view, name='flashcards'),
    path('saved-flashcards/', saved_flashcards_view, name='saved_flashcards'),
]