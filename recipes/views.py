from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Recipe
from .forms import RecipeForm


class RecipeListView(ListView):
    """Display a list of all recipes."""
    model = Recipe
    template_name = 'recipes/recipe_list.html'
    context_object_name = 'recipes'
    paginate_by = 10
    ordering = ['name']


class RecipeDetailView(DetailView):
    """Display details of a single recipe."""
    model = Recipe
    template_name = 'recipes/recipe_detail.html'
    context_object_name = 'recipe'


class RecipeCreateView(CreateView):
    """Create a new recipe."""
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/recipe_form.html'
    success_url = reverse_lazy('recipe-list')

    def form_valid(self, form):
        """Add success message on successful form submission."""
        response = super().form_valid(form)
        return response


class RecipeUpdateView(UpdateView):
    """Update an existing recipe."""
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/recipe_form.html'
    success_url = reverse_lazy('recipe-list')

    def form_valid(self, form):
        """Add success message on successful form update."""
        response = super().form_valid(form)
        return response


class RecipeDeleteView(DeleteView):
    """Delete a recipe."""
    model = Recipe
    template_name = 'recipes/recipe_confirm_delete.html'
    success_url = reverse_lazy('recipe-list')
    context_object_name = 'recipe'
