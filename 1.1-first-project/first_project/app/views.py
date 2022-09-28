from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
import os

def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.now()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    list_files = os.listdir('app')
    files = []
    for number, file in enumerate(list_files):
        if number != len(list_files)-1:
            files.append(file + ', ')
        else:
            files.append(file)
    return HttpResponse(files)

