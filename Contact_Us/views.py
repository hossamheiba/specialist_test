from django.shortcuts import render, get_object_or_404

from .models import ContactUs
from Our_Center.models import MapLocation

def loc_view(request):
    locations = MapLocation.objects.all()
    contact = ContactUs.objects.first()
    context = {
        'locations': [
            {
                'title': location.title,
                'description': location.description,
                'latitude': location.latitude,
                'longitude': location.longitude,
                'address': location.address,
                'image': location.image.url if location.image else None,
                'url': location.url
            }
            for location in locations
        ],
        "contact" : contact
    }
    return render(request, 'Contact_Us.html', context)
