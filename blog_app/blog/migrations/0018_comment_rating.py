# Generated by Django 2.1.5 on 2019-04-19 08:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20190419_0338'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
    ]
