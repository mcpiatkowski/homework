from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('recipes/', views.getRecipes, name='recipes'),
    path('recipes/<str:pk>/', views.getRecipeDetail, name='recipe-detail'),
    path('ingredients/', views.getIngredients, name='ingredients'),
]
