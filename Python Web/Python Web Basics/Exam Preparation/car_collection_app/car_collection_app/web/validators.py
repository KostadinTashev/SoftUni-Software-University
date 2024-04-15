from django.core.exceptions import ValidationError


def validate_username_at_least_2_chars(value):
    if len(value) < 2:
        raise ValidationError('The username must be a minimum of 2 chars')


def validate_year_between_1980_and_2049(value):
    if not 1980 <= value <= 2049:
        raise ValidationError('Year must be between 1980 and 2049')
