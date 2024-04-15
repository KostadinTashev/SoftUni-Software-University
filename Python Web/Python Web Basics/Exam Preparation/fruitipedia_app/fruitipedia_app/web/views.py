from django.shortcuts import render, redirect

from fruitipedia_app.web.forms import CreateProfileForm, CreateFruitForm, EditFruitForm, DeleteFruitForm, \
    EditProfileForm, DeleteProfileForm
from fruitipedia_app.web.models import Profile, Fruit


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def get_fruits():
    try:
        return Fruit.objects.all()
    except Fruit.DoesNotExist:
        return None


def get_fruit(pk):
    try:
        return Fruit.objects.get(pk=pk)
    except Fruit.DoesNotExist:
        return None


def index(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(request, 'index.html', context)


def dashboard(request):
    profile = get_profile()
    fruits = get_fruits()
    context = {
        'profile': profile,
        'fruits': fruits,
    }
    return render(request, 'dashboard.html', context)


def add_fruit(request):
    profile = get_profile()
    if request.method == 'GET':
        form = CreateFruitForm()
    else:
        form = CreateFruitForm(request.POST)
        if form.is_valid():
            form.instance.owner = profile
            form.save()
            return redirect('dashboard')
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'create-fruit.html', context)


def details_fruit(request, pk):
    profile = get_profile()
    fruit = get_fruit(pk)
    context = {
        'profile': profile,
        'fruit': fruit,
    }
    return render(request, 'details-fruit.html', context)


def edit_fruit(request, pk):
    profile = get_profile()
    fruit = get_fruit(pk)
    if request.method == 'GET':
        form = EditFruitForm(instance=fruit)
    else:
        form = EditFruitForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'profile': profile,
        'fruit': fruit,
        'form': form,
    }
    return render(request, 'edit-fruit.html', context)


def delete_fruit(request, pk):
    profile = get_profile()
    fruit = get_fruit(pk)
    if request.method == 'GET':
        form = DeleteFruitForm(instance=fruit)
    else:
        form = DeleteFruitForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            fruit.delete()
            return redirect('dashboard')
    context = {
        'profile': profile,
        'fruit': fruit,
        'form': form,
    }
    return render(request, 'delete-fruit.html', context)


def add_profile(request):
    profile = get_profile()
    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'create-profile.html', context)


def details_profile(request):
    profile = get_profile()
    fruits = get_fruits().count()
    context = {
        'profile': profile,
        'fruits': fruits,
    }
    return render(request, 'details-profile.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    fruits = get_fruits()
    if request.method == 'GET':
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)
        form.save()
        for fruit in fruits:
            fruit_form = DeleteFruitForm(request.POST, instance=fruit)
            fruit_form.save()
        return redirect('index')
    context = {
        'profile': profile,
        'fruits': fruits,
        'form': form,
    }
    return render(request, 'delete-profile.html', context)
