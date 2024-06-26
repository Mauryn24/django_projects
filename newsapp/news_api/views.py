# news_api/views.py

import hashlib
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
import requests
from django.views.decorators.csrf import csrf_protect
from .models import Like, Bookmark, Article
from django.utils.dateparse import parse_datetime


API_KEY = '0a47c0fd4f15448481f3fb46f8eecae3'

# Existing views...
# news_api/views.py


def home(request):
    country = request.GET.get('country')
    category = request.GET.get('category')

    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
    else:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'

    response = requests.get(url)
    data = response.json()
    articles = data['articles']

    # Generate unique IDs for articles if they don't have one
    for article in articles:
        article_id = hashlib.md5(article['url'].encode('utf-8')).hexdigest()
        article['id'] = article_id

        # Handle missing published_at
        published_at = article.get('publishedAt')
        if published_at:
            article['published_at'] = parse_datetime(published_at)
        else:
            article['published_at'] = None

    # Pagination
    paginator = Paginator(articles, 5)  # Show 5 articles per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
        'articles': page_obj.object_list,
    }

    return render(request, 'news_api/home.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'news_api/signup.html', {'form': form})

@csrf_protect
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'news_api/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def like_article(request, article_id):
    article_data = None
    for article in request.session.get('articles', []):
        if article['id'] == article_id:
            article_data = article
            break

    if article_data:
        article, created = Article.objects.get_or_create(
            id=article_id,
            defaults={
                'title': article_data['title'],
                'description': article_data.get('description', ''),
                'url': article_data['url'],
                'urlToImage': article_data.get('urlToImage', ''),
                'published_at': article_data.get('published_at'),
                'author': article_data.get('author', ''),
            }
        )
        Like.objects.create(user=request.user, article=article)
    
    return redirect('home')

@login_required
def bookmark_article(request, article_id):
    article_data = None
    for article in request.session.get('articles', []):
        if article['id'] == article_id:
            article_data = article
            break

    if article_data:
        try:
            article, created = Article.objects.get_or_create(
                id=article_id,
                defaults={
                    'title': article_data['title'],
                    'description': article_data.get('description', ''),
                    'url': article_data['url'],
                    'urlToImage': article_data.get('urlToImage', ''),
                    'published_at': article_data.get('published_at'),
                    'author': article_data.get('author', ''),
                }
            )
            Bookmark.objects.create(user=request.user, article=article)
        except IntegrityError:
            # Handle if the article already exists
            pass
    
    return redirect('home')

@login_required
def remove_like_article(request, article_id):
    article = Article.objects.get(id=article_id)
    Like.objects.filter(user=request.user, article=article).delete()
    return redirect('liked_articles')

@login_required
def remove_bookmark_article(request, article_id):
    article = Article.objects.get(id=article_id)
    Bookmark.objects.filter(user=request.user, article=article).delete()
    return redirect('bookmarked_articles')

@login_required
def liked_articles(request):
    likes = Like.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'news_api/liked_articles.html', {'likes': likes})

@login_required
def bookmarked_articles(request):
    bookmarks = Bookmark.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'news_api/bookmarked_articles.html', {'bookmarks': bookmarks})