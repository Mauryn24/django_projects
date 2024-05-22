from django.urls import path
from FlavourQuest import views

urlpatterns = [
    path('home/', views.home, name='home'),
]