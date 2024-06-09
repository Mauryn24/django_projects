from django.shortcuts import render, redirect
from django.contrib import messages
from twilio.rest import Client
from geopy.geocoders import Nominatim

# Twilio configuration
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
twilio_number = 'your_twilio_number'
client = Client(account_sid, auth_token)

# Geolocator configuration
geolocator = Nominatim(user_agent="gbv_support_app")

# Sample emergency contacts
emergency_contacts = [
    {"name": "National Helpline", "phone": "+1234567890"},
    {"name": "Local Shelter", "phone": "+0987654321"}
]

def home(request):
    # Home page
    return render(request, 'home.html')

def resources(request):
    # Information resources page
    return render(request, 'resources.html')

def emergency_contacts_page(request):
    # Emergency contacts page
    return render(request, 'emergency_contacts.html', {'contacts': emergency_contacts})

def send_alert(request):
    # Send alert message to emergency contacts
    if request.method == 'POST':
        try:
            user_location = request.POST['location']
            message_body = f"ALERT! GBV Incident Reported. Location: {user_location}"
            for contact in emergency_contacts:
                client.messages.create(
                    body=message_body,
                    from_=twilio_number,
                    to=contact['phone']
                )
            messages.success(request, "Alert sent successfully!")
        except Exception as e:
            messages.error(request, f"Failed to send alert: {e}")
        return redirect('home')

def get_location(request):
    # Get user's current location
    return render(request, 'get_location.html')

def find_shelters(request):
    # Find nearby shelters
    if request.method == 'POST':
        address = request.POST['address']
        location = geolocator.geocode(address)
        if location:
            shelters = [
                {"name": "Shelter One", "address": "123 Safe St, City", "distance": "2 km"},
                {"name": "Shelter Two", "address": "456 Secure Ave, City", "distance": "5 km"}
            ]
            return render(request, 'shelters.html', {'shelters': shelters, 'user_location': location.address})
        else:
            messages.error(request, "Location not found. Please try again.")
            return redirect('get_location')
