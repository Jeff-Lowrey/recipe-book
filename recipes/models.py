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