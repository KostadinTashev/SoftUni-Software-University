from django.core.exceptions import ValidationError


def validate_menu_categories(value):
    for category in ["Appetizers", "Main Course", "Desserts"]:
        if category.lower() not in value.lower():
            raise ValidationError(
                message=f'The menu must include each of the categories "Appetizers", "Main Course", "Desserts".')
