from django.shortcuts import render, redirect

from eventer_app.web.forms import CreateProfileForm, CreateEventForm, EditEventForm, DeleteEventForm, EditProfileForm, \
    DeleteProfileForm
from eventer_app.web.models import Profile, Event


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def get_events():
    try:
        return Event.objects.all()
    except Event.DoesNotExist:
        return None


def get_event(pk):
    return Event.objects.get(pk=pk)


def index(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(request, 'shared/home-page.html', context)


def dashboard(request):
    profile = get_profile()
    events = get_events()

    context = {
        'profile': profile,
        'events': events,
    }

    return render(request, 'events/dashboard.html', context)


def add_event(request):
    profile = get_profile()

    if request.method == 'GET':
        form = CreateEventForm()
    else:
        form = CreateEventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'events/event-create.html', context)


def details_event(request, pk):
    profile = get_profile()
    event = get_event(pk=pk)
    context = {
        'profile': profile,
        'event': event,
    }
    return render(request, 'events/events-details.html', context)


def edit_event(request, pk):
    profile = get_profile()
    event = get_event(pk=pk)
    if request.method == 'GET':
        form = EditEventForm(instance=event)
    else:
        form = EditEventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'form': form,
        'profile': profile,
        'event': event,
    }
    return render(request, 'events/event-edit.html', context)


def delete_event(request, pk):
    profile = get_profile()
    event = get_event(pk=pk)

    if request.method == 'GET':
        form = DeleteEventForm(instance=event)
    else:
        form = DeleteEventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'profile': profile,
        'event': event,
        'form': form,
    }

    return render(request, 'events/events-delete.html', context)


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
    return render(request, 'profiles/profile-create.html', context)


def details_profile(request):
    profile = get_profile()
    events = get_events()
    context = {
        'profile': profile,
        'events': events.count(),
    }
    return render(request, 'profiles/profile-details.html', context)


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
    return render(request, 'profiles/profile-edit.html', context)


def delete_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'profiles/profile-delete.html', context)
