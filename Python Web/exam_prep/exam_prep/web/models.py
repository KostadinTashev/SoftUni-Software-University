from enum import Enum

from django.core import validators, exceptions
from django.db import models

from exam_prep.web.validators import validate_only_alphanumeric


class Profile(models.Model):
    MIN_LENGTH_USERNAME = 2
    MAX_LENGTH_USERNAME = 15

    username = models.CharField(
        max_length=MAX_LENGTH_USERNAME,
        validators=[
            validators.MinLengthValidator(MIN_LENGTH_USERNAME),
            validate_only_alphanumeric,
        ],
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )


class ChoicesEnum(Enum):
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]


class AlbumGenres(ChoicesEnum):
    POP = 'Pop Music'
    JAZZ = 'Jazz Music'
    RNB = 'R&B Music'
    ROCK = 'Rock Music'
    COUNTRY = 'Country Music'
    DANCE = 'Dance Music'
    HIP_HOP = 'Hip Hop Music'
    OTHER = 'Other'



class Album(models.Model):
    MAX_LENGTH_NAME = 30
    MAX_LENGTH_ARTIST = 30
    MAX_LENGTH_GENRE = 30

    album_name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        unique=True,
        null=False,
        blank=False,
        verbose_name='Album Name',
    )

    artist = models.CharField(
        max_length=MAX_LENGTH_ARTIST,
        null=False,
        blank=False,
    )

    genre = models.CharField(
        max_length=MAX_LENGTH_GENRE,
        null=False,
        blank=False,
        choices=AlbumGenres.choices(),
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL',
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(0.0),
        )
    )

    class Meta:
        ordering = ('pk',)

# Without enums
# class Album(models.Model):
#     MAX_LENGTH_NAME = 30
#     MAX_LENGTH_ARTIST = 30
#     MAX_LENGTH_GENRE = 30
#     # GENRE_CHOICES = (
#     #     ('Pop Music', 'Pop Music'),
#     #     ('Jazz Music', 'Jazz Music'),
#     #     ('R&B Music', 'R&B Music'),
#     #     ('Rock Music', 'Rock Music'),
#     #     ('Country Music', 'Country Music'),
#     #     ('Dance Music', 'Dance Music'),
#     #     ('Hip Hop Music', 'Hip Hop Music'),
#     #     ('Other Music', 'Other Music'),
#     # )
#     POP_MUSIC = 'Pop Music'
#     JAZZ_MUSIC = 'Jazz Music'
#     RNB_MUSIC = 'R&B Music'
#     ROCK_MUSIC = 'Rock Music'
#     COUNTRY_MUSIC = 'Country Music'
#     DANCE_MUSIC = 'Dance Music'
#     HIP_HOP_MUSIC = 'Hip Hop Music'
#     OTHER_MUSIC = 'Other Music'
#     MUSICS = (
#         (POP_MUSIC, POP_MUSIC),
#         (JAZZ_MUSIC, JAZZ_MUSIC),
#         (RNB_MUSIC, RNB_MUSIC),
#         (ROCK_MUSIC, ROCK_MUSIC),
#         (COUNTRY_MUSIC, COUNTRY_MUSIC),
#         (DANCE_MUSIC, DANCE_MUSIC),
#         (HIP_HOP_MUSIC, HIP_HOP_MUSIC),
#         (OTHER_MUSIC, OTHER_MUSIC),
#     )
#
#     album_name = models.CharField(
#         max_length=MAX_LENGTH_NAME,
#         unique=True,
#         null=False,
#         blank=False,
#         verbose_name='Album Name',
#     )
#
#     artist = models.CharField(
#         max_length=MAX_LENGTH_ARTIST,
#         null=False,
#         blank=False,
#     )
#
#     genre = models.CharField(
#         max_length=MAX_LENGTH_GENRE,
#         null=False,
#         blank=False,
#         choices=MUSICS,
#     )
#
#     description = models.TextField(
#         null=True,
#         blank=True,
#     )
#
#     image_url = models.URLField(
#         null=False,
#         blank=False,
#         verbose_name='Image URL',
#     )
#
#     price = models.FloatField(
#         null=False,
#         blank=False,
#         validators=(
#             validators.MinValueValidator(0.0),
#         )
#     )
#
#     class Meta:
#         ordering = ('pk',)
