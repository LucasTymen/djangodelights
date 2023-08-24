from django.db import models

# Create your models here.

class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=40, unique=True),
    av_quantity = models.IntegerField(),
    price_per_unit = models.IntegerField(),


class MenuItem(models.Model):
    menu_item_name = models.CharField(max_length=40),
    menu_price = models.FloatField(default=0)


class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey("app.Model", verbose_name=_("menu_item"), on_delete=models.CASCADE),
    quantity = models.ForeignKey("app.Model", verbose_name=_("quantity"), on_delete=models.CASCADE)


class Purchase(models.Model):
    date_purchase = models.DateTimeField()
