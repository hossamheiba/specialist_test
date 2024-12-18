from django.shortcuts import render
from .models import AboutSection

def about_view(request):
    about_section = AboutSection.objects.first()
    context = {
        'about_section': about_section
    }
    return render(request, 'About_Us.html', context)
