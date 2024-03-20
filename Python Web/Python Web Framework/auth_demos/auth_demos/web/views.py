# from django.contrib.auth.models import User
import random
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.shortcuts import render, redirect

from auth_demos.web.models import Article

UserModel = get_user_model()


@login_required
def index(request):
    suffix = random.randint(1, 1000)

    # Not a good idea:
    # UserModel.objects.create(...)

    # Good idea:
    user = UserModel.objects.create_user(
        username=f'kostadin_{suffix}',
        password='admin123'
    )
    # print('-' * 20)
    # print(request.user)
    # login(request, user)
    # print(request.user)
    # print('-' * 20)
    # lenovo = UserModel.objects.get(username='lenovo')
    kostadin_125 = UserModel.objects.get(username='kostadin_125')
    context = {
        'user': request.user,
        'permission': request.user.has_perm('auth.view_user'),
        'kostadin_125': kostadin_125.has_perm('auth.view_user'),
        'xss': '<script>alert("Hacked")</script>',
    }

    print(Article.objects.raw('Select * FROM Articles'))

    return render(request, 'index.html', context)


class IndexView(views.TemplateView, LoginRequiredMixin):
    template_name = 'index.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        pass


def login_user(request):
    # Authentication
    user = authenticate(
        username=f'kostadin_125',
        password='admin123'
    )

    # Authorization
    login(request, user)  # Does `request.user = user` + other stuff

    print(f'Authenticated user: {user}')

    return redirect('index')


def logout_user(request):
    logout(request)
    return redirect('index')
