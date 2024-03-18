from django.shortcuts import render, redirect

from fruitipedia_app.web.forms import ProfileCreateForm, FruitCreateForm
from fruitipedia_app.web.models import Profile, Fruit


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def get_fruits():
    return Fruit.objects.all()


def get_fruit(pk):
    return Fruit.objects.get(pk=pk)


def index(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(request, 'core/index.html', context)


def dashboard(request):
    profile = get_profile()
    fruits = get_fruits()

    context = {
        'profile': profile,
        'fruits': fruits,
    }

    return render(request, 'core/dashboard.html', context)


def create_fruit(request):
    profile = get_profile()

    if request.method == 'GET':
        form = FruitCreateForm()
    else:
        form = FruitCreateForm(request.POST)
        if form.is_valid():
            form.instance.owner = profile
            form.save()
        return redirect('dashboard')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'fruit/create-fruit.html', context)


def details_fruit(request, pk):
    profile = get_profile()
    fruit = get_fruit(pk=pk)

    context = {
        'profile': profile,
        'fruit': fruit,
    }

    return render(request, 'fruit/details-fruit.html', context)


def edit_fruit(request, pk):
    return render(request, 'fruit/edit-fruit.html')


def delete_fruit(request, pk):
    return render(request, 'fruit/delete-fruit.html')


def create_profile(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('dashboard')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profile/create-profile.html', context)


def details_profile(request):
    return render(request, 'profile/details-profile.html')


def edit_profile(request):
    return render(request, 'profile/edit-profile.html')


def delete_profile(request):
    return render(request, 'profile/delete-profile.html')
