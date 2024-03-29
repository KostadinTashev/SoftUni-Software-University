# Generated by Django 5.0.2 on 2024-02-25 20:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_accesscard_employeesprojects'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('parent_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='web.category')),
            ],
        ),
    ]
