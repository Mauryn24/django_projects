from django.urls import path
from . import views


urlpatterns = [
    # make sure the name included in the views.home ie the home is the same name in the functiom created in the views.py
    path('', views.home, name='hello_world-base'),
]
