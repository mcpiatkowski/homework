from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', views.MyTokenRefreshView.as_view(), name='token_refresh'),

    path('recipes/', views.getRecipes, name='recipes'),
    path('recipe/<str:pk>/', views.getRecipeDetail, name='recipe-detail'),
    path('ingredients/', views.getIngredients, name='ingredients'),

    path('recipe/<str:pk>/ingredients/',
         views.getRecipeIngredients, name='recipe-ingredients'),
]
