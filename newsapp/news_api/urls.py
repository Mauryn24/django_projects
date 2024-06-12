# news_api/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('like/<str:article_id>/', views.like_article, name='like_article'),
    path('bookmark/<str:article_id>/', views.bookmark_article, name='bookmark_article'),
    path('remove_like/<str:article_id>/', views.remove_like_article, name='remove_like_article'),
    path('remove_bookmark/<str:article_id>/', views.remove_bookmark_article, name='remove_bookmark_article'),
    path('liked/', views.liked_articles, name='liked_articles'),
    path('bookmarked/', views.bookmarked_articles, name='bookmarked_articles'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
