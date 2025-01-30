# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
class CarMake(models.Model):
    CountryOption ={
        ('US', 'US'),
        ('UK', 'UK'),
        ('JP', 'JP'),
        ('IN', 'IN'),
        ('CA', 'CA'),
        ('AU', 'AU'),
        ('FR', 'FR'),
        ('DE', 'DE'),
    }
# - Name
    name = models.CharField(max_length=50)
    description = models.TextField()
    country = models.CharField(max_length=50,choices=CountryOption,default='US')
# - __str__ method to print a car make object
    def __str__(self):
        return self.name


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
class CarModel(models.Model):
    TypeChoice = {
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'WAGON'),
        ('COUPE', 'COUPE'),
        ('CONVERTIBLE', 'CONVERTIBLE'),
        ('HATCHBACK', 'HATCHBACK'),
        ('MINIVAN', 'MINIVAN'),
        ('PICKUP', 'PICKUP'),
        ('SPORTS CAR', 'SPORTS CAR'),
        ('OTHER', 'OTHER')
    }
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
    name = models.CharField(max_length=50)
    dealer_id = models.IntegerField()
    type = models.CharField(max_length=50,choices=TypeChoice,default='Sedan')
    year = models.IntegerField(validators=[MaxValueValidator(2023), MinValueValidator(2015)])
    seat = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(2)])

    def __str__(self):
        return self.name
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
