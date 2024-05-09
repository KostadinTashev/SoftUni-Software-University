from django.shortcuts import render, redirect

from tasty_recipes_app.web.forms import CreateProfileForm, CreateRecipeForm, EditRecipeForm, DeleteRecipeForm, \
    EditProfileForm, DeleteProfileForm
from tasty_recipes_app.web.models import Profile, Recipe


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def get_recipes():
    try:
        return Recipe.objects.all()
    except Recipe.DoesNotExist:
        return None


def get_recipe(recipe_id):
    return Recipe.objects.get(pk=recipe_id)


def home_page(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(request, 'home-page.html', context)


def catalogue(request):
    profile = get_profile()
    recipes = get_recipes()
    context = {
        'profile': profile,
        'recipes': recipes,
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
    return render(request, 'create-profile.html', context)


def details_profile(request):
    profile = get_profile()
    recipes_count = get_recipes().count()
    context = {
        'profile': profile,
        'recipes_count': recipes_count,
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
    recipes = get_recipes()
    if request.method == 'GET':
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)
        form.save()
        if form.is_valid():
            for recipe in recipes:
                recipe_form = DeleteRecipeForm(request.POST, instance=recipe)
                recipe_form.save()
        return redirect('home page')
    context = {
        'profile': profile,
        'recipes': recipes,
        'form': form,
    }
    return render(request, 'delete-profile.html', context)


def create_recipe(request):
    profile = get_profile()
    if request.method == 'GET':
        form = CreateRecipeForm()
    else:
        form = CreateRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'create-recipe.html', context)


def details_recipe(request, recipe_id):
    profile = get_profile()
    recipe = get_recipe(recipe_id)
    recipe_ingredients = recipe.ingredients.split(', ')

    context = {
        'profile': profile,
        'recipe': recipe,
        'recipe_ingredients': recipe_ingredients,
    }
    return render(request, 'details-recipe.html', context)


def edit_recipe(request, recipe_id):
    profile = get_profile()
    recipe = get_recipe(recipe_id)
    if request.method == 'GET':
        form = EditRecipeForm(instance=recipe)
    else:
        form = EditRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'profile': profile,
        'recipe': recipe,
        'form': form,
    }
    return render(request, 'edit-recipe.html', context)


def delete_recipe(request, recipe_id):
    profile = get_profile()
    recipe = get_recipe(recipe_id)
    if request.method == 'GET':
        form = DeleteRecipeForm(instance=recipe)
    else:
        form = DeleteRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'profile': profile,
        'recipe': recipe,
        'form': form,
    }
    return render(request, 'delete-recipe.html', context)
