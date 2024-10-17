from django.apps import AppConfig


class RecipesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recipes'
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('add/', views.add_recipe, name='add_recipe'),
]
