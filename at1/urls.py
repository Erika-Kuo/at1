from django.contrib import admin
from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt
from eduprod.views import index, flashcards_view, saved_flashcards
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('eduprod/', include(('eduprod.urls', 'eduprod'), namespace='eduprod')),
    path('accounts/login/', include('users.urls')),
    path('', csrf_exempt(index), name='index'),
    path('flashcards/', flashcards_view, name='flashcards'),
    path('saved-flashcards/', saved_flashcards, name='saved_flashcards'),
]
