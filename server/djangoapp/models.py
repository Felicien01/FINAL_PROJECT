from django.db import models
from django.utils.timezone import now


# Create your models here.

class CarMake(models.Model):
    name = models.CharField(null=False, max_length=100)
    description = models.CharField(max_length=500)
    def __str__(self):
        return "Name: " + self.name + "," + \
                 "Description: " + self.description


class CarModel(models.Model):
    name = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer = models.IntegerField()
    Sedan = 'sd'
    SUV = 'suv'
    WAGON = 'wg'
    TYPE_CHOICES = [
        (Sedan, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'WAGON'),
    ]
    Type = models.CharField(
        max_length=3,
        choices=TYPE_CHOICES,
    )
    year = models.DateField()
    def __str__(self):
        return "Name: " + self.name + "," + \
                 "Model: " + self.dealer +' ' + self.Type +' ' + self.year 


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
