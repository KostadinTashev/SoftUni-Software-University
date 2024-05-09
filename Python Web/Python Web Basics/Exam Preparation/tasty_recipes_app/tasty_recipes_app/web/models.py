from django.core import validators
from django.db import models

from tasty_recipes_app.web.validators import validate_string_at_least_2_char, validate_string_starts_with_capital_letter


class Profile(models.Model):
    MIN_LENGTH_NICKNAME = 2
    MAX_LENGTH_NICKNAME = 20
    MAX_LENGTH_FIRST_NAME = 30
    MAX_LENGTH_LAST_NAME = 30

    nickname = models.CharField(
        max_length=MAX_LENGTH_NICKNAME,
        validators=(validate_string_at_least_2_char,),
        unique=True,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_LENGTH_FIRST_NAME,
        validators=(validate_string_starts_with_capital_letter,),
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_LAST_NAME,
        validators=(validate_string_starts_with_capital_letter,),
        null=False,
        blank=False,
    )

    chef = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )

    bio = models.TextField(
        null=True,
        blank=True,
    )


class Recipe(models.Model):
    MIN_LENGTH_RECIPE = 10
    MAX_LENGTH_RECIPE = 100
    MAX_LENGTH_CUISINE_TYPE = 7
    MIN_VALUE_COOKING_TIME = 1
    CUISINE_TYPE_CHOICES = (
        ('French', 'French'),
        ('Chinese', 'Chinese'),
        ('Italian', 'Italian'),
        ('Balkan', 'Balkan'),
        ('Other', 'Other')
    )

    title = models.CharField(
        max_length=MAX_LENGTH_RECIPE,
        validators=(validators.MinLengthValidator(MIN_LENGTH_RECIPE),),
        unique=True,
        null=False,
        blank=False
    )

    cuisine_type = models.CharField(
        max_length=MAX_LENGTH_CUISINE_TYPE,
        choices=CUISINE_TYPE_CHOICES,
        null=False,
        blank=False,
    )

    ingredients = models.TextField(
        null=False,
        blank=False,
        help_text='Ingredients must be separated by a comma and space.',
    )

    instructions = models.TextField(
        null=False,
        blank=False,
    )

    cooking_time = models.PositiveIntegerField(
        validators=(validators.MinValueValidator(MIN_VALUE_COOKING_TIME),),
        null=False,
        blank=False,
        help_text='Provide the cooking time in minutes.',
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )
