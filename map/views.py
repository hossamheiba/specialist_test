from django.shortcuts import render, redirect
from .models import Location

def select_location(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

        if latitude and longitude:
            location = Location.objects.create(
                name=name,
                latitude=latitude,
                longitude=longitude
            )
            return redirect('/')  # وجه المستخدم لصفحة النجاح أو عرض آخر

    return render(request, 'map.html')
