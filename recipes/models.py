from django.db import models

# Create your models here.


class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    english_quantity = models.DecimalField(max_digits=10, decimal_places=2)
    metric_quantity = models.IntegerField()
    ENGLISH_UNIT_CHOICES = [
        ("tsp", "teaspoon"),
        ("tablespoon", "tbsp"),
        ("cup", "cup"),
        ("gallon", "gal."),
        ("ounce", "oz"),
        ("fluid ounce", "fl oz"),
        ("pound", "lb"),
    ]
    METRIC_UNIT_CHOICES = [
        ("gram", "g"),
        ("kilogram", "kg"),
        ("milliliter", "mL"),
        ("liter", "L"),
    ]
    UNIT_CHOICES = ENGLISH_UNIT_CHOICES + METRIC_UNIT_CHOICES
    unit_type = models.CharField(max_length=50, choices=UNIT_CHOICES)

    def unit_consistency(self) -> None:
        pass


class Step(models.Model):
    ACTION_CHOICES = [
        ("stir", "Stir"),
        ("mix", "Mix"),
        ("cream", "Cream"),
        ("blend", "Blend"),
        ("whisk", "Whisk"),
        ("puree", "Puree"),
        ("whip", "Whip"),
        ("fold", "Fold"),
        ("add", "Add"),
    ]
    COOKING_METHOD_CHOICES = [
        ("bake", "Bake"),
        ("boil", "Boil"),
        ("steam", "Steam"),
        ("roast", "Roast."),
        ("braise", "Braise"),
        ("fry", "Fry"),
        ("airfry", "Air Fry"),
        ("stirfry", "Stir Fry"),
    ]
    step_number = models.IntegerField()
    description = models.CharField(max_length=1000)
    step_ingredient = models.ManyToManyField(
        Ingredient,
    )
    cooking_method = models.CharField(max_length=50, choices=COOKING_METHOD_CHOICES)
    step_action = models.CharField(max_length=50, choices=ACTION_CHOICES)


class Recipe(models.Model):
    FLAVOR_PROFILE_CHOICES = [
        ("sweet", "Sweet"),
        ("sour", "Sour"),
        ("salty", "Salty"),
        ("bitter", "Bitter"),
        ("umami", "Umami"),
        ("spicy", "Spicy"),
        ("acidic", "Acidic"),
        ("vibrant", "Vibrant"),
        ("delicate", "Delicate"),
        ("asian", "Asian"),
        ("mexican", "Mexican"),
        ("thai", "Thai"),
        ("indian", "Indian"),
        ("italian", "Italian"),
        ("mediterranean", "Mediterranean"),
        ("slavic", "Slavic"),
        ("russian", "Russian"),
        ("jewish", "Jewish"),
        ("british", "British"),
        ("weird", "Weird"),
    ]

    name = models.CharField(max_length=200)
    style = models.CharField(max_length=100)
    flaver_profile = models.CharField(max_length=50, choices=FLAVOR_PROFILE_CHOICES)

    ingredients = models.ManyToManyField(Ingredient)
    steps = models.ManyToManyField(Step)
