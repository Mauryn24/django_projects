import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from .models import Recipe, Category, Comment, Favorite, Cart
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def fetch_categories():
    response = requests.get(
        'https://api.spoonacular.com/recipes/cuisines',
        params={'apiKey': settings.SPOONACULAR_API_KEY}
    )
    data = response.json()
    return data['cuisines']

def fetch_dishes_by_category(category):
    response = requests.get(
        'https://api.spoonacular.com/recipes/complexSearch',
        params={'cuisine': category, 'apiKey': settings.SPOONACULAR_API_KEY}
    )
    data = response.json()
    return data['results']

def fetch_recipes(query):
    response = requests.get(
        'https://api.spoonacular.com/recipes/complexSearch',
        params={'query': query, 'apiKey': settings.SPOONACULAR_API_KEY}
    )
    return response.json().get('results', [])

def index(request):
    categories = Category.objects.all()
    return render(request, 'Flavourquest/index.html', {'categories': categories})

def search(request):
    query = request.GET.get('q')
    recipes = fetch_recipes(query)
    return render(request, 'Flavourquest/search.html', {'recipes': recipes})

def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    recipes = Recipe.objects.filter(category=category)
    return render(request, 'Flavourquest/category_detail.html', {'category': category, 'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, api_id=recipe_id)  # Use API ID
    comments = recipe.comment_set.all()
    return render(request, 'Flavourquest/recipe_detail.html', {'recipe': recipe, 'comments': comments})

@login_required
def add_comment(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        Comment.objects.create(user=request.user, recipe=recipe, content=content)
    return redirect('recipe_detail', recipe_id=recipe_id)

@login_required
def add_to_cart(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    Cart.objects.create(user=request.user, recipe=recipe)
    return redirect('recipe_detail', recipe_id=recipe_id)

@login_required
def add_to_favorites(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    Favorite.objects.create(user=request.user, recipe=recipe)
    return redirect('recipe_detail', recipe_id=recipe_id)

@login_required
def like_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.user in recipe.likes.all():
        recipe.likes.remove(request.user)
    else:
        recipe.likes.add(request.user)
    return redirect('recipe_detail', recipe_id=recipe_id)
