from django import forms

from .models import Recipe


class RecipeForm(forms.ModelForm):
    """Form for creating and editing Recipe instances."""

    class Meta:
        model = Recipe
        fields = ["name", "style", "flaver_profile", "ingredients", "steps"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter recipe name"}
            ),
            "style": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter recipe style"}
            ),
            "flaver_profile": forms.CheckboxSelectMultiple(),
            "ingredients": forms.CheckboxSelectMultiple(),
            "steps": forms.CheckboxSelectMultiple(),
        }
        labels = {
            "name": "Recipe Name",
            "style": "Cooking Style",
            "flaver_profile": "Flavor Profile",
            "ingredients": "Ingredients",
            "steps": "Steps",
        }
        help_texts = {
            "name": "Enter a descriptive name for your recipe",
            "style": "E.g., Italian, Chinese, Fusion, etc.",
            "flaver_profile": "Select all flavor profiles that apply",
            "ingredients": "Select the ingredients for this recipe",
            "steps": "Select the steps for this recipe",
        }
