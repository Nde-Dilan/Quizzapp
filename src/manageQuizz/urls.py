from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = "manageQuizz"
urlpatterns = [
    path('quizz/', getquizz, name='quizz'),
    path('quizz/<int:pk>', QuizzDetailView.as_view(), name='detail'),
    path('question/<int:question>', question, name='question'),
]