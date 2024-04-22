# users/views.py

from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse

def user_profile(request, username=None):
    if username is None:
        # If no username is provided, display the current user's profile
        if request.user.is_authenticated:
            profile = request.user.profile
            return render(request, 'users/profile.html', {'profile': profile})
        else:
            return HttpResponse('Please log in to view your profile', status=401)
    else:
        # Retrieve the profile of the specified user
        try:
            user = User.objects.get(username=username)
            profile = user.profile
            return render(request, 'users/profile.html', {'profile': profile})
        except User.DoesNotExist:
            return HttpResponse('User not found', status=404)
