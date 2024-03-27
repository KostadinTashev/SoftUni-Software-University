import random

from django import forms
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.core.cache import cache
# from django.views.decorators.cache import cache_page
from django.views import generic as views

from signals_middlewares_cache_session_demos.web.models import Task

UserModel = get_user_model()


# @cache_page(5 * 60)
def index(request):
    request.session['count'] = request.session.get('count', 0) + 1

    if not cache.get('users'):
        cache.set('users', UserModel.objects.all(), 5)

    users = cache.get('users')

    prev_tasks_id = request.session.get('prev_tasks', [])

    context = {
        # 'count': random.randint(1, 10000),
        'count': request.session['count'],
        'users': users,
        'tasks': Task.objects.all(),
        'prev_tasks': Task.objects.filter(pk__in=prev_tasks_id),
    }

    return render(request, 'index.html', context)


def create_task(request):
    Task.objects.create(title=f'Title {random.randint(1, 10000)}')
    return redirect('index')


def details_task(request, pk):
    task = Task.objects.filter(pk=pk).get()

    prev_tasks = request.session.get('prev_tasks', [])
    prev_tasks.append(task.pk)
    start_index = max(0, len(prev_tasks) - 3)
    request.session.set_expiry(5 * 60)
    request.session['prev_tasks'] = prev_tasks[start_index:]

    return redirect('index')
