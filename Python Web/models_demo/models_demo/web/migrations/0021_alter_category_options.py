# Generated by Django 5.0.2 on 2024-02-26 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0020_alter_employee_options_department_created_on_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
