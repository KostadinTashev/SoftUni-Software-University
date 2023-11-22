from django.contrib import admin

from main_app.models import Director, Actor, Movie


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'birth_date', 'nationality']
    list_filter = ['years_of_experience']
    search_fields = ['full_name', 'nationality']
    search_help_text = 'Search director by Full Name and Nationality'


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'birth_date', 'nationality']
    list_filter = ['is_awarded']
    search_fields = ['full_name']
    readonly_fields = ['last_updated']
    search_help_text = 'Search Actor by Full Name'


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'storyline', 'rating', 'director']
    list_filter = ['is_awarded', 'is_classic', 'genre']
    search_fields = ['title', 'director__full_name']
    readonly_fields = ['last_updated']
    search_help_text = "Search Movie by Title and Director's Full Name "
