from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# news_api/models.py

class Article(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    url = models.URLField()
    url_to_image = models.URLField(null=True, blank=True)
    published_at = models.DateTimeField()
    source_name = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
