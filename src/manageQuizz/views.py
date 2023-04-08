<<<<<<< HEAD
from django.shortcuts import render
from django.views.generic import DetailView
from manageQuizz.models import *


# Create your views here.


def getquizz(request):
    quizzs = Quizz.objects.all()
    # print(quizzs)
    return render(request, 'manageQuizz/quizz.html', {"quizz": quizzs})

class QuizzDetailView(DetailView):
    model = Quizz
    template_name = "manageQuizz/detail.html"
    context_object_name = "qz"

def question(request,question):
    """Cette vue est dédié à une questions et des reponses"""
    print("question")
    print(question)
    # qz=Question.objects.filter(quizz.id==question)
    #Donc il faut recuperer les proposition et la question liée a celles ci.

=======
from django.shortcuts import render
from django.views.generic import DetailView
from manageQuizz.models import *


# Create your views here.


def getquizz(request):
    quizzs = Quizz.objects.all()
    # print(quizzs)
    return render(request, 'manageQuizz/quizz.html', {"quizz": quizzs})

class QuizzDetailView(DetailView):
    model = Quizz
    template_name = "manageQuizz/detail.html"
    context_object_name = "qz"

def question(request,question):
    """Cette vue est dédié à une questions et des reponses"""
    print("question")
    print(question)
    # qz=Question.objects.filter(quizz.id==question)
    #Donc il faut recuperer les proposition et la question liée a celles ci.

>>>>>>> debdd121a0ae1b44b1acc4613d7d9b75efb8eeb7
    return render(request,'manageQuizz/question.html',{"all_qz_proposition":all_qz_proposition,"qz":qz})