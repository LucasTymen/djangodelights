from django.db import models

# Create your models here.
class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length="40"),
    available_quantity = models.IntegerField(default=0),
    prices_per_unit = models.FloatField(default=0),

class MenuItem(models.Model):
    menu_item = models.CharField(max_length="40"),
    price_set = models.FloatField(default=0),
