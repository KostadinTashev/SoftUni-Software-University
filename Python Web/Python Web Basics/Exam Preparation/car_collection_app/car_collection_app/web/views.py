from django.shortcuts import render, redirect

from car_collection_app.web.forms import CreateProfileForm, CreateCarForm, EditCarForm, DeleteCarForm, EditProfileForm, \
    DeleteProfileForm
from car_collection_app.web.models import Profile, Car


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def get_cars():
    try:
        return Car.objects.all()
    except Car.DoesNotExist:
        return None


def get_car(pk):
    try:
        return Car.objects.get(pk=pk)
    except Car.DoesNotExist:
        return None


def index(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(request, 'index.html', context)


def catalogue(request):
    profile = get_profile()
    cars = get_cars()
    context = {
        'profile': profile,
        'cars': cars,
        'cars_count': cars.count(),
    }
    return render(request, 'catalogue.html', context)


def create_profile(request):
    profile = get_profile()
    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'profile-create.html', context)


def details_profile(request):
    profile = get_profile()
    cars = get_cars()
    total_price = 0
    for car in cars:
        total_price += car.price
    context = {
        'profile': profile,
        'total_price': total_price,
    }
    return render(request, 'profile-details.html', context)


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
    return render(request, 'profile-edit.html', context)


def delete_profile(request):
    profile = get_profile()
    cars = get_cars()
    if request.method == 'GET':
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)
        form.save()
        if form.is_valid():
            for car in cars:
                car_form = DeleteCarForm(request.POST, instance=car)
                car_form.save()
        return redirect('index')
    context = {
        'profile': profile,
        'cars': cars,
        'form': form,
    }
    return render(request, 'profile-delete.html', context)


def create_car(request):
    profile = get_profile()
    if request.method == 'GET':
        form = CreateCarForm()
    else:
        form = CreateCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'car-create.html', context)


def details_car(request, pk):
    profile = get_profile()
    car = get_car(pk=pk)
    context = {
        'profile': profile,
        'car': car,
    }
    return render(request, 'car-details.html', context)


def edit_car(request, pk):
    profile = get_profile()
    car = get_car(pk=pk)
    if request.method == 'GET':
        form = EditCarForm(instance=car)
    else:
        form = EditCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'profile': profile,
        'car': car,
        'form': form,
    }
    return render(request, 'car-edit.html', context)


def delete_car(request, pk):
    profile = get_profile()
    car = get_car(pk)
    if request.method == 'GET':
        form = DeleteCarForm(instance=car)
    else:
        form = DeleteCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'profile': profile,
        'car': car,
        'form': form,
    }
    return render(request, 'car-delete.html', context)
