from django.db import models
from django.core.validators import RegexValidator, MinValueValidator

class DVD(models.Model):
    title = models.CharField(max_length=100,unique=True)
    category = models.CharField(max_length=50)
    runTime = models.IntegerField(default = 0, validators=[MinValueValidator(0)])
    year = models.IntegerField(default = 0, validators=[MinValueValidator(0)])
    price = models.FloatField(default = 0, validators=[MinValueValidator(0)])