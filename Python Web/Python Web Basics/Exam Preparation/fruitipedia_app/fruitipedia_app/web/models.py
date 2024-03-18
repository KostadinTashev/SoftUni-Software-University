from django.core import validators
from django.db import models

from fruitipedia_app.web.validators import validate_name


class Profile(models.Model):
    MAX_LENGTH_FIRST_NAME = 25
    MIN_LENGTH_FIRST_NAME = 2
    MAX_LENGTH_LAST_NAME = 35
    MIN_LENGTH_LAST_NAME = 1
    MAX_LENGTH_EMAIL = 40
    MAX_LENGTH_PASSWORD = 20
    MIN_LENGTH_PASSWORD = 8

    first_name = models.CharField(
        max_length=MAX_LENGTH_FIRST_NAME,
        validators=(validators.MinLengthValidator(MIN_LENGTH_FIRST_NAME),
                    validate_name,),
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_LAST_NAME,
        validators=(validators.MinLengthValidator(MIN_LENGTH_LAST_NAME),
                    validate_name,),
        null=False,
        blank=False,
    )

    email = models.EmailField(
        max_length=MAX_LENGTH_EMAIL,
        unique=True,
        null=False,
        blank=False,
    )

    password = models.CharField(
        max_length=MAX_LENGTH_PASSWORD,
        validators=(validators.MinLengthValidator(MIN_LENGTH_PASSWORD),),
        null=False,
        blank=False,
        help_text='Password length requirements: 8 to 20 characters',
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )

    age = models.IntegerField(
        null=True,
        blank=True,
        default=18,
    )


class Fruit(models.Model):
    MAX_LENGTH_NAME = 30
    MIN_LENGTH_NAME = 2

    name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        validators=(validators.MinLengthValidator(MIN_LENGTH_NAME),),
        unique=True,
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

    nutrition = models.TextField(
        null=True,
        blank=True,
    )

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        blank=True,
        null=False,
    )
