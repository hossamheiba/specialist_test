from django.shortcuts import render
from .models import *

def news_section_view(request):
    slider = NewsSliderSection.objects.prefetch_related('news_sliders').first()
    news = NewsSection.objects.prefetch_related('news_cards').all()
    context = {
        "news": news,
        "slider": slider,
    }
    return render(request, "News.html", context)



