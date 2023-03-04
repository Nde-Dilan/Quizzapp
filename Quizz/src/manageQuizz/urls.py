from django.contrib import admin
from django.urls import path, include

from manageQuizz.views import getquizz

urlpatterns = [
    path('quizz/', getquizz, name='manageQuizz-quizz')
]