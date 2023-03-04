from django.shortcuts import render

from manageQuizz.models import *


# Create your views here.

def getquizz(request):
    quizzs = Quizz.objects.all()
    print(quizzs)
    return render(request, 'manageQuizz/quizz.html', {"quizz": quizzs})
