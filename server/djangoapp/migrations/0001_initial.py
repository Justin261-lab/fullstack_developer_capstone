# Generated by Django 5.1.5 on 2025-01-30 15:42

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarMake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('country', models.CharField(choices=[('CA', 'CA'), ('AU', 'AU'), ('JP', 'JP'), ('UK', 'UK'), ('DE', 'DE'), ('FR', 'FR'), ('US', 'US'), ('IN', 'IN')], default='US', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('dealer_id', models.IntegerField()),
                ('type', models.CharField(choices=[('Sedan', 'Sedan'), ('CONVERTIBLE', 'CONVERTIBLE'), ('SPORTS CAR', 'SPORTS CAR'), ('SUV', 'SUV'), ('MINIVAN', 'MINIVAN'), ('PICKUP', 'PICKUP'), ('HATCHBACK', 'HATCHBACK'), ('COUPE', 'COUPE'), ('OTHER', 'OTHER'), ('WAGON', 'WAGON')], default='Sedan', max_length=50)),
                ('year', models.IntegerField(validators=[django.core.validators.MaxValueValidator(2023), django.core.validators.MinValueValidator(2015)])),
                ('seat', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(2)])),
                ('car_make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoapp.carmake')),
            ],
        ),
    ]
