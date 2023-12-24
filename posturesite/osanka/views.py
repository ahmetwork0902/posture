from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import UserRegisterForm
from .models import Users
menu = [{'title': "О нас", 'url_name': 'about'},
        {'title': "Достижения", 'url_name': 'achievements'},
        {'title': "Статистика", 'url_name': 'statistics'},
        {'title': "Войти", 'url_name': 'kabinet'}
]
from django.views.generic import CreateView
from .models import *
import sys
sys.path.append('C:/Users/reieg/OneDrive/Рабочий стол/GITLAB/posture_app/backend/model')
# from mediapipe_camera_use import main_func

# def index(request):
#     return render(request, 'osanka/index.html')

# Главная длинная страница
def index(request):
    return render(request, 'osanka/start_page.html')


#страница начала отслеживания
def start(request):
    return render(request,
                  'osanka/start.html')

# Страница достижений
@login_required
def achievements(request):
    print(request.GET)
    data = dict()
    return render(request,
                  'osanka/achievements.html')

def start_total_start(request):
    # main_func()
    return render(request,
                  'osanka/achievements.html')

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена<h1>")

