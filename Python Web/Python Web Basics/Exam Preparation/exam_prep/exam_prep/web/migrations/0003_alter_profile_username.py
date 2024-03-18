# Generated by Django 5.0.3 on 2024-03-06 10:31

import django.core.validators
import exam_prep.web.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_album'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), exam_prep.web.models.validate_only_alphanumeric]),
        ),
    ]