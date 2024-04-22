# urls.py

from django.urls import path
from trips.views import trip_detail, redirect_to_first_trip

urlpatterns = [
    path('', redirect_to_first_trip, name='homepage_redirect'),
    path('trips/<int:trip_id>/', trip_detail, name='trip_detail'),
]
