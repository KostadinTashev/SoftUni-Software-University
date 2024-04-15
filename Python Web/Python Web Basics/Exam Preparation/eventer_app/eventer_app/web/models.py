from django.core import validators
from django.db import models

from eventer_app.web.validators import validate_only_letters, validate_at_least_one_digit, validate_not_in_past


class Profile(models.Model):
    MAX_LEN_FIRST_NAME = 20
    MIN_LEN_LAST_NAME = 4
    MAX_LEN_LAST_NAME = 30
    MAX_LEN_EMAIL = 45
    MIN_LEN_PASSWORD = 5
    MAX_LEN_PASSWORD = 20

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        validators=(validate_only_letters,),
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        validators=(validators.MinLengthValidator(MIN_LEN_LAST_NAME),),
        null=False,
        blank=False,
    )

    email = models.EmailField(
        max_length=MAX_LEN_EMAIL,
        null=False,
        blank=False,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    password = models.CharField(
        max_length=MAX_LEN_PASSWORD,
        validators=(validators.MinLengthValidator(MIN_LEN_PASSWORD),
                    validate_at_least_one_digit,),
        null=False,
        blank=False,
    )


class Event(models.Model):
    MIN_LEN_EVENT_NAME = 2
    MAX_LEN_EVENT_NAME = 30
    CATEGORY_CHOICES = (
        ('Sports', 'Sports'),
        ('Festivals', 'Festivals'),
        ('Conferences', 'Conferences'),
        ('Performing Art', 'Performing Art'),
        ('Concerts', 'Concerts'),
        ('Theme Party', 'Theme Party'),
        ('Other', 'Other'),
    )

    event_name = models.CharField(
        max_length=MAX_LEN_EVENT_NAME,
        validators=(validators.MinLengthValidator(MIN_LEN_EVENT_NAME),),
        null=False,
        blank=False,
    )

    category = models.CharField(
        null=False,
        blank=False,
        choices=CATEGORY_CHOICES,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    date = models.DateField(
        validators=(validate_not_in_past,),
        null=False,
        blank=False,
    )

    event_image = models.URLField(
        null=False,
        blank=False,
    )
