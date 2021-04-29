from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Recipe, Ingredient


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class MyRecipeSerializer(serializers.ModelSerializer):
    recipe_ingredients = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Recipe
        fields = '__all__'

    def get_recipe_ingredients(self, obj):
        recipe_ingredients = obj.ingredients.all()
        serializer = IngredientSerializer(recipe_ingredients, many=True)
        return serializer.data
