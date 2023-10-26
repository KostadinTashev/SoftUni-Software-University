# Generated by Django 4.2.6 on 2023-10-25 14:03

from django.db import migrations


def set_price(apps, schema_editor):
    MULTIPLY_PRICE = 120

    smartphone_model = apps.get_model('main_app', 'Smartphone')
    smartphones = smartphone_model.objects.all()

    for smartphone in smartphones:
        smartphone.price = len(smartphone.brand) * MULTIPLY_PRICE
    smartphone_model.objects.bulk_update(smartphones, ['price'])


def set_category(apps, schema_editor):
    smartphone_model = apps.get_model('main_app', 'Smartphone')
    smartphones = smartphone_model.objects.all()
    for smartphone in smartphones:
        if smartphone.price >= 750:
            smartphone.category = 'Expensive'
        else:
            smartphone.category = 'Cheap'
    smartphone_model.objects.bulk_update(smartphones, ['category'])


def set_price_category(apps, schema_editor):
    set_price(apps, schema_editor)
    set_category(apps, schema_editor)


def reverse_price_and_category(apps, schema_editor):
    smartphone_model = apps.get_model('main_app', 'Smartphone')
    smartphones = smartphone_model.objects.all()
    for smartphone in smartphones:
        smartphone.price = 0
        smartphone.category = "empty"
        smartphone.save()


class Migration(migrations.Migration):
    dependencies = [
        ('main_app', '0013_smartphone'),
    ]

    operations = [migrations.RunPython(set_price_category, reverse_code=reverse_price_and_category)
                  ]