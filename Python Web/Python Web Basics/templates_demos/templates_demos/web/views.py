import random
from datetime import datetime

from django.shortcuts import render, redirect


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f'Name: {self.name}; Age: {self.age}'


def index(request):
    context = {
        'title': 'SoftUni Home Page',
        'value': random.random(),
        'info': {
            'address': 'Sofia'
        },
        'student': Student('Kostadin', 21),
        'student_info': Student('Kostadin', 21).get_info(),
        'now': datetime.now(),
        'students': ['Pesho', 'Pesho', 'Gosho', 'Maria', 'Stamat'],
        'values': list(range(1, 20)),
        # 'students': []
    }

    return render(request, 'index.html', context)


def redirect_to_home(request):
    return redirect('index')


def about(request):
    return render(request, 'about.html')
