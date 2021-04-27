from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('recipes/', views.getRecipes, name='recipes'),
    path('recipes/<str:pk>/', views.getRecipeDetail, name='recipe-detail'),
    path('ingredients/', views.getIngredients, name='ingredients'),
]
