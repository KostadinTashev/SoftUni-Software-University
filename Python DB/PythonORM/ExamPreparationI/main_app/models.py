from django.core import validators
from django.db import models

from main_app.managers import DirectorManager
from main_app.mixins import Person, Award, LastUpdated


class Director(Person):
    years_of_experience = models.SmallIntegerField(
        validators=[
            validators.MinValueValidator(0)
        ],
        default=0
    )

    objects = DirectorManager()

    def __str__(self):
        return f'Director: {self.full_name}'


class Actor(Person, Award, LastUpdated):
    def __str__(self):
        return f'Actor: {self.full_name}'


class Movie(Award, LastUpdated):
    class GenreChoices(models.TextChoices):
        ACTION = 'Action',
        COMEDY = 'Comedy',
        DRAMA = 'Drama',
        OTHER = 'Other'

    title = models.CharField(
        max_length=150,
        validators=[
            validators.MinLengthValidator(5),
        ]
    )
    release_date = models.DateField()
    storyline = models.TextField(
        null=True,
        blank=True,
    )
    genre = models.CharField(
        max_length=6,
        choices=GenreChoices.choices,
        default=GenreChoices.OTHER,
    )
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[
            validators.MinValueValidator(0.0),
            validators.MaxValueValidator(10.0)
        ],
        default=0.0
    )
    is_classic = models.BooleanField(
        default=False,
    )
    director = models.ForeignKey(
        to=Director,
        on_delete=models.CASCADE,
        related_name='director_movies'
    )
    starring_actor = models.ForeignKey(
        to=Actor,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='starring_movies'
    )
    actors = models.ManyToManyField(
        to=Actor,
        related_name='actor_movies'
    )

    def __str__(self):
        return f'Movie: {self.title}'
