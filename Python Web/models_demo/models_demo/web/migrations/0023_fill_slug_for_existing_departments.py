# Generated by Django 5.0.2 on 2024-02-26 19:22

from django.db import migrations
from django.utils.text import slugify


def add_slugs(apps, schema_editor):
    Department = apps.get_model('web', 'Department')
    departments = Department.objects.all()
    for department in departments:
        department.slug = slugify(department.name)
    Department.objects.bulk_update(departments, ['slug'])


def delete_slug(apps, schema_editor):
    Department = apps.get_model('web', 'Department')
    departments = Department.objects.all()
    for department in departments:
        department.slug = None

    Department.objects.bulk_update(departments, ['slug'])


class Migration(migrations.Migration):
    dependencies = [
        ('web', '0022_department_slug'),
    ]

    operations = [
        migrations.RunPython(add_slugs, delete_slug),
    ]
