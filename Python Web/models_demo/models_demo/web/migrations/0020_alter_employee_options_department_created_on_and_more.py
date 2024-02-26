# Generated by Django 5.0.2 on 2024-02-26 17:32

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0019_alter_employee_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ('years_of_experience', '-age')},
        ),
        migrations.AddField(
            model_name='department',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='department',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='project',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
