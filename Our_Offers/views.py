from django.shortcuts import render
from .models import OfferSliderSection, OfferSection

def offer_section_view(request):
    slider = OfferSliderSection.objects.prefetch_related('offer_sliders').first()
    offers = OfferSection.objects.prefetch_related('offer_cards').all()
    context = {
        "offers": offers,
        "slider": slider,
    }
    return render(request, "Offers.html", context)
