# trips/views.py

from django.shortcuts import render, redirect
from .models import Trip
from django.http import HttpResponse

def trip_detail(request, trip_id):
    try:
        trip = Trip.objects.get(pk=trip_id)
        return render(request, 'trips/trip_detail.html', {'trip': trip})
    except Trip.DoesNotExist:
        return HttpResponse('Trip not found', status=404)


# views.py

from django.shortcuts import redirect
from trips.models import Trip

def redirect_to_first_trip(request):
    # Retrieve the first trip (or any logic you prefer)
    trip = Trip.objects.first()
    if trip:
        return redirect('trip_detail', trip_id=trip.id)
    else:
        # Handle the case when no trip is found
        return HttpResponse('No trips found', status=404)


