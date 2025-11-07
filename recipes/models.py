from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField()
    english_quantity = models.DecimalField()
    metric_quantity = models.IntegerField()
    ENGLISH_UNIT_CHOICES = [
    ("tsp","teaspoon"),
    ("tablespoon","tbsp"),
    ("cup","cup")
    ("gallon","gal."),
    ("ounce","oz"),
    ("fluid ounce","fl oz"),
    ("pound","lb")
    ]
    METRIC_UNIT_CHOICES = [
    ("gram", "g"),
    ("kilogram", "kg"),
    ("milliliter", "mL"),
    ("liter", "L"),
    ]
    UNIT_CHOICES = ENGLISH_UNIT_CHOICES+METRIC_UNIT_CHOICES
    unit_type = models.CharField(choices=UNIT_CHOICES)
    

    def unit_consistency(self):
        pass

class Step(models.Model):
    step_no = models.IntegerField()
    step_description = models.CharField()
    step_ingredient = user = models.OneToOneField(
        Ingredient,
        on_delete=models.CASCADE,
    )


class Recipe(models.Model):

    COOKING_METHOD_CHOICES = [
    ("bake","Bake"),
    ("boil","Boil"),
    ("steam","Steam")
    ("roast","Roast."),
    ("braise","Braise"),
    ("fry","Fry"),
    ("airfry","Air Fry"),
    ("stirfry","Stir Fry"),
    ]
    name = models.CharField()
    style = models.CharField()
    flaver_profile = models.ArrayField()
    cooking_method = models.CharField(hcoices=COOKING_METHOD_CHOICES)   
    ingredients = models.ManyToManyField(Ingredient)
    steps = models.ManyToManyField(Step)

    
    