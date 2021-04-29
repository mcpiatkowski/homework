from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .models import Recipe, Ingredient
from .serializers import RecipeSerializer, IngredientSerializer, MyRecipeSerializer

from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.views import TokenRefreshView
from datetime import timedelta


class MyTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        data['exp'] = timedelta(minutes=1)

        return data


class MyTokenRefreshView(TokenRefreshView):
    serializer_class = MyTokenRefreshSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getRecipes(request):
    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getRecipeDetail(request, pk):
    recipe = Recipe.objects.get(id=pk)
    serializer = MyRecipeSerializer(recipe, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getIngredients(request):
    ingredients = Ingredient.objects.all()
    serializer = IngredientSerializer(ingredients, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getRecipeIngredients(request, pk):
    recipe = Recipe.objects.get(id=pk)
    recipe_ingredients = recipe.ingredients.all()
    print(recipe_ingredients)
    serializer = MyRecipeSerializer(recipe, many=False)
    return Response(serializer.data)

# context={'request': request}
