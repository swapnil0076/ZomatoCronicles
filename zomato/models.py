from django.db import models

# Create your models here.

class Dish(models.Model):
    dish_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    availability =  models.BooleanField(default=False)

