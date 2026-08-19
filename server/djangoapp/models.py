from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # if it's luxury, utiity, sport, general
    BRAND_CATEGORIES = [
        ('GENERAL', 'General'),
        ('LUXURY', 'Luxury'),
    ]
    category = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name  # Return the name as the string representation


class CarModel(models.Model):
    # Many-to-One relationship
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('MINIVAN', 'Minivan'),
        ('COUPE', 'Coupe'),
        ('HATCHBACK', 'Hatchback'),
        ('CONVERTIBLE', 'Convertible'),
        ('PICKUP', 'Pickup'),
    ]
    type = models.CharField(max_length=20, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(
                                default=2023,
                                validators=[
                                    MaxValueValidator(2023),
                                    MinValueValidator(2015)
                                ])

    def __str__(self):
        return self.name  # Return the name as the string representation
