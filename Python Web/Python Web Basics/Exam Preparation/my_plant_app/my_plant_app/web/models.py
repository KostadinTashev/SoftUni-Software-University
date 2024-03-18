from django.core import validators
from django.db import models

from my_plant_app.web.validators import validate_name, validate_only_letters


class Profile(models.Model):
    MAX_LENGTH_USERNAME = 10
    MIN_LENGTH_USERNAME = 2
    MAX_LENGTH_FIRST_NAME = 20
    MAX_LENGTH_LAST_NAME = 20

    username = models.CharField(
        max_length=MAX_LENGTH_USERNAME,
        validators=(validators.MinLengthValidator(MIN_LENGTH_USERNAME),),
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_LENGTH_FIRST_NAME,
        validators=(validate_name,),
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_LAST_NAME,
        validators=(validate_name,),
        null=False,
        blank=False,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class Plant(models.Model):
    MAX_LENGTH_PLANT_TYPE = 14
    MAX_LENGTH_NAME = 20
    MIN_LENGTH_NAME = 2

    PLANT_TYPE_CHOICES = (
        ('Outdoor Plants', 'Outdoor Plants'),
        ('Indoor Plants', 'Indoor Plants'),
    )

    plant_type = models.CharField(
        max_length=MAX_LENGTH_PLANT_TYPE,
        choices=PLANT_TYPE_CHOICES,
        null=False,
        blank=False,
    )

    name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        validators=(validators.MinLengthValidator(MIN_LENGTH_NAME),
                    validate_only_letters,
                    ),
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
    )
