# Generated by Django 5.0.2 on 2024-03-01 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_person_alter_todo_priority_todo_assignee'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
