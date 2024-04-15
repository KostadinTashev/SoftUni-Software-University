from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_only_letters(value):
    if not value.isalpha():
        raise ValidationError('The name should contain only letters!')


def validate_at_least_one_digit(value):
    if not any(char.isdigit() for char in value):
        raise ValidationError('The password must contain at least 1 digit!')


def validate_not_in_past(value):
    if value < timezone.now().date():
        raise ValidationError('The date cannot be in the past!')
