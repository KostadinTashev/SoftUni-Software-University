# Generated by Django 5.0.2 on 2024-02-25 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_alter_employee_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(editable=False, max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='level',
            field=models.CharField(choices=[('Junior', 'Junior'), ('Regular', 'Regular'), ('Senior', 'Senior')], max_length=7, verbose_name='Seniority level'),
        ),
    ]
