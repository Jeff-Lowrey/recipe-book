"""
URL configuration for recipe_book project.
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("recipes/", include("recipes.urls")),
]
