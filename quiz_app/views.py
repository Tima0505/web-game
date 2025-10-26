from django.shortcuts import render
from .models import Question

def home(request):
    return render(request, 'quiz_app/home.html')

def quiz_game(request):
    questions = Question.objects.all()
    return render(request, 'quiz_app/quiz_game.html', {'questions': questions})
