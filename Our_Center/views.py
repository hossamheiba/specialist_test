from .models import *
from django.shortcuts import render, get_object_or_404



def map_view(request):
    our_center = get_object_or_404(OurCenterSection)
    center = get_object_or_404(InformationOurCenter)
    locations = MapLocation.objects.all()
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
        'our_center': our_center,
        'center': center,
    }
    return render(request, 'Our_Center.html', context)
