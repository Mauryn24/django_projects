from django.core.management.base import BaseCommand
from FlavourQuest.models import Category, Recipe
import requests
from django.conf import settings

class Command(BaseCommand):
    help = 'Fetch and store categories and dishes from Spoonacular API'

    def fetch_recipes(self, query):
        response = requests.get(
            'https://api.spoonacular.com/recipes/complexSearch',
            params={'query': query, 'apiKey': settings.SPOONACULAR_API_KEY, 'number': 100}
        )
        data = response.json()
        return data.get('results', [])

    def handle(self, *args, **kwargs):
        queries = ['Italian', 'Chinese', 'Mexican', 'Indian', 'American']  # Example queries/categories
        for query in queries:
            category, created = Category.objects.get_or_create(name=query)
            recipes = self.fetch_recipes(query)
            for recipe in recipes:
                Recipe.objects.update_or_create(
                    api_id=recipe['id'],  # Use API ID
                    defaults={
                        'title': recipe['title'],
                        'ingredients': '',
                        'instructions': '',
                        'category': category
                    }
                )
        self.stdout.write(self.style.SUCCESS('Successfully fetched and stored categories and dishes'))
