from django.db import models

# Create your models here.

class Dish(models.Model):
    dish_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    availability =  models.BooleanField(default=False)
    description = models.TextField(default='Your default description here')

    def __str__(self):
        return self.name

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    order_status = models.CharField(max_length=20, default='preparing')
    dishes = models.ManyToManyField(Dish)

    def __str__(self):
        return self.customer_name