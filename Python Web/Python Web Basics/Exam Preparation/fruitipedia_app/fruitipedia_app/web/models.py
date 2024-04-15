from django.core import validators
from django.db import models

from fruitipedia_app.web.validators import validate_starts_with_letter


class Profile(models.Model):
    MIN_LENGTH_FIRST_NAME = 2
    MAX_LENGTH_FIRST_NAME = 25
    MIN_LENGTH_LAST_NAME = 1
    MAX_LENGTH_LAST_NAME = 35
    MAX_LENGTH_EMAIL = 40
    MIN_LENGTH_PASSWORD = 8
    MAX_LENGTH_PASSWORD = 20

    first_name = models.CharField(
        max_length=MAX_LENGTH_FIRST_NAME,
        validators=(validators.MinLengthValidator(MIN_LENGTH_FIRST_NAME),
                    validate_starts_with_letter,),
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_LAST_NAME,
        validators=(validators.MinLengthValidator(MIN_LENGTH_LAST_NAME),
                    validate_starts_with_letter,),
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
        help_text='*Password length requirements: 8 to 20 characters',
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )

    age = models.IntegerField(
        default=18,
        null=True,
        blank=True,
    )


class Fruit(models.Model):
    MIN_LENGTH_NAME = 2
    MAX_LENGTH_NAME = 30

    name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        validators=(validators.MinLengthValidator(MIN_LENGTH_NAME),),
        unique=True,
        null=False,
        blank=False,
        error_messages='This fruit name is already in use! Try a new one.',
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
        to=Profile,
        on_delete=models.CASCADE,
    )
