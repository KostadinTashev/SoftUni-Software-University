from django.core import validators
from django.db import models

from car_collection_app.web.validators import validate_username_at_least_2_chars, validate_year_between_1980_and_2049


class Profile(models.Model):
    MIN_LENGTH_USERNAME = 2
    MAX_LENGTH_USERNAME = 10
    MIN_AGE = 18
    MAX_LENGTH_PASSWORD = 30
    MAX_LENGTH_FIRST_NAME = 30
    MAX_LENGTH_LAST_NAME = 30

    username = models.CharField(
        max_length=MAX_LENGTH_USERNAME,
        validators=(validators.MinLengthValidator(MIN_LENGTH_USERNAME),
                    validate_username_at_least_2_chars,),
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        validators=(validators.MinValueValidator(MIN_AGE),),
        null=False,
        blank=False,
    )

    password = models.CharField(
        max_length=MAX_LENGTH_PASSWORD,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_LENGTH_FIRST_NAME,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_LAST_NAME,
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class Car(models.Model):
    TYPE_CHOICES = (
        ('Sports Car', 'Sports Car'),
        ('Pickup', 'Pickup'),
        ('Crossover', 'Crossover'),
        ('Minibus', 'Minibus'),
        ('Other', 'Other'),
    )
    MAX_LENGTH_TYPE = 10
    MIN_LENGTH_MODEL = 2
    MAX_LENGTH_MODEL = 20
    MIN_PRICE = 1.0

    type = models.CharField(
        max_length=MAX_LENGTH_TYPE,
        choices=TYPE_CHOICES,
        null=False,
        blank=False,
    )

    model = models.CharField(
        max_length=MAX_LENGTH_MODEL,
        validators=(validators.MinLengthValidator(MIN_LENGTH_MODEL),),
        null=False,
        blank=False,
    )

    year = models.IntegerField(
        validators=(validate_year_between_1980_and_2049,),
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        validators=(validators.MinValueValidator(MIN_PRICE),),
        null=False,
        blank=False,
    )
