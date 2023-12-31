# Generated by Django 5.0 on 2023-12-23 14:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctorapi', '0009_remove_doctor_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='hospitals',
            field=models.ManyToManyField(blank=True, to='doctorapi.hospital'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='insurance_companies',
            field=models.ManyToManyField(blank=True, to='doctorapi.insurancecompany'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='average_rating',
            field=models.IntegerField(default=2, max_length=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]
