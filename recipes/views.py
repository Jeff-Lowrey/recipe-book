from typing import Any

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import RecipeForm
from .models import Recipe


class RecipeListView(ListView[Recipe]):
    """Display a list of all recipes."""

    model = Recipe
    template_name = "recipes/recipe_list.html"
    context_object_name = "recipes"
    paginate_by = 10
    ordering = ["name"]


class RecipeDetailView(DetailView[Recipe]):
    """Display details of a single recipe."""

    model = Recipe
    template_name = "recipes/recipe_detail.html"
    context_object_name = "recipe"


class RecipeCreateView(CreateView[Recipe, RecipeForm]):
    """Create a new recipe."""

    model = Recipe
    form_class = RecipeForm
    template_name = "recipes/recipe_form.html"
    success_url = reverse_lazy("recipe-list")

    def form_valid(self, form: RecipeForm) -> HttpResponse:
        """Add success message on successful form submission."""
        response = super().form_valid(form)
        return response


class RecipeUpdateView(UpdateView[Recipe, RecipeForm]):
    """Update an existing recipe."""

    model = Recipe
    form_class = RecipeForm
    template_name = "recipes/recipe_form.html"
    success_url = reverse_lazy("recipe-list")

    def form_valid(self, form: RecipeForm) -> HttpResponse:
        """Add success message on successful form update."""
        response = super().form_valid(form)
        return response


class RecipeDeleteView(DeleteView[Recipe, Any]):
    """Delete a recipe."""

    model = Recipe
    template_name = "recipes/recipe_confirm_delete.html"
    success_url = reverse_lazy("recipe-list")
    context_object_name = "recipe"
