from django.urls import path

from .views import (
    RecipeCreateView,
    RecipeDeleteView,
    RecipeDetailView,
    RecipeListView,
    RecipeUpdateView,
)

urlpatterns = [
    path("", RecipeListView.as_view(), name="recipe-list"),
    path("recipe/<int:pk>/", RecipeDetailView.as_view(), name="recipe-detail"),
    path("recipe/new/", RecipeCreateView.as_view(), name="recipe-create"),
    path("recipe/<int:pk>/edit/", RecipeUpdateView.as_view(), name="recipe-update"),
    path("recipe/<int:pk>/delete/", RecipeDeleteView.as_view(), name="recipe-delete"),
]
