# Generated by Django 5.0.2 on 2024-02-22 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='level',
            field=models.CharField(default='asd', max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
