from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('resources/', views.resources, name='resources'),
    path('emergency_contacts/', views.emergency_contacts_page, name='emergency_contacts'),
    path('send_alert/', views.send_alert, name='send_alert'),
    path('get_location/', views.get_location, name='get_location'),
    path('find_shelters/', views.find_shelters, name='find_shelters'),
]
