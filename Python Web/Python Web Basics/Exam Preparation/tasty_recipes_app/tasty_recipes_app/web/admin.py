from django.contrib import admin

from tasty_recipes_app.web.models import Profile, Recipe


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    pass
