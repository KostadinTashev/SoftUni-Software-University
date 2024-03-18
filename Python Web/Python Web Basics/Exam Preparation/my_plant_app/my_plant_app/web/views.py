from django.shortcuts import render, redirect

from my_plant_app.web.forms import ProfileCreateForm, PlantCreateForm, PlantEditForm, PlantDeleteForm, ProfileEditForm, \
    ProfileDeleteForm
from my_plant_app.web.models import Profile, Plant


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def get_plants():
    try:
        return Plant.objects.all()
    except Plant.DoesNotExist:
        return None


def get_plant(pk):
    return Plant.objects.filter(pk=pk).get()


def index(request):
    profile = get_profile()

    context = {
        'profile': profile,
    }

    return render(request, 'core/home-page.html', context)


def catalogue(request):
    profile = get_profile()
    plants = get_plants()
    context = {
        'profile': profile,
        'plants': plants,
    }
    return render(request, 'core/catalogue.html', context)


def create_profile(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('catalogue')

    context = {
        'form': form,
    }

    return render(request, 'profile/create-profile.html', context)


def details_profile(request):
    profile = get_profile()
    plants = get_plants()
    context = {
        'profile': profile,
        'plants': plants,
    }
    return render(request, 'profile/profile-details.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
        return redirect('details profile')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profile/edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    plants = get_plants()
    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        form.save()
        for plant in plants:
            plant_form = PlantDeleteForm(request.POST, instance=plant)
            plant_form.save()
        return redirect('index')

    context = {
        'form': form,
        'profile': profile,
        'plants': plants,
    }

    return render(request, 'profile/delete-profile.html', context)


def create_plant(request):
    profile = get_profile()
    if request.method == 'GET':
        form = PlantCreateForm()
    else:
        form = PlantCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('catalogue')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'plant/create-plant.html', context)


def details_plant(request, pk):
    profile = get_profile()
    plant = get_plant(pk)

    context = {
        'profile': profile,
        'plant': plant
    }
    return render(request, 'plant/plant-details.html', context)


def edit_plant(request, pk):
    profile = get_profile()
    plant = get_plant(pk)
    if request.method == 'GET':
        form = PlantEditForm(instance=plant)
    else:
        form = PlantEditForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
        return redirect('catalogue')

    context = {
        'form': form,
        'plant': plant,
        'profile': profile,
    }

    return render(request, 'plant/edit-plant.html', context)


def delete_plant(request, pk):
    profile = get_profile()
    plant = get_plant(pk)
    if request.method == 'GET':
        form = PlantDeleteForm(instance=plant)
    else:
        form = PlantDeleteForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'profile': profile,
        'plant': plant,
        'form': form,
    }

    return render(request, 'plant/delete-plant.html', context)
