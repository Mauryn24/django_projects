from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/<int:recipe_id>/add_comment/', views.add_comment, name='add_comment'),
    path('recipe/<int:recipe_id>/add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('recipe/<int:recipe_id>/add_to_favorites/', views.add_to_favorites, name='add_to_favorites'),
    path('recipe/<int:recipe_id>/like/', views.like_recipe, name='like_recipe'),
]
