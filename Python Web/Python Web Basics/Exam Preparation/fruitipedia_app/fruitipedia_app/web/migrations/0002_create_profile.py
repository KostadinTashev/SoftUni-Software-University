import django.core.validators
import fruitipedia_app.web.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25, validators=[django.core.validators.MinLengthValidator(2),
                                                                           fruitipedia_app.web.validators.validate_name])),
                ('last_name', models.CharField(max_length=35, validators=[django.core.validators.MinLengthValidator(1),
                                                                          fruitipedia_app.web.validators.validate_name])),
                ('email', models.EmailField(max_length=40, unique=True)),
                ('password',
                 models.CharField(help_text='Password length requirements: 8 to 20 characters', max_length=20,
                                  validators=[django.core.validators.MinLengthValidator(8)])),
                ('image_url', models.URLField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, default=18, null=True)),
            ],
        ),
    ]
