from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def getRecipes(request):
    return Response({"message": "Recipe List"})


@api_view(['GET'])
def getRecipeDetail(request, pk):
    return Response({"message": "Recipe Detail"})


@api_view(['GET'])
def getIngredients(request):
    return Response({"message": "Ingredients!"})
