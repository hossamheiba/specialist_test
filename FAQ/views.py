from django.shortcuts import render
from .models import FaqSection, FAQ

def faq_view(request):
    faq_section = FaqSection.objects.first()  # Get the first FAQ section
    faqs = FAQ.objects.filter(faq_section=faq_section) if faq_section else FAQ.objects.none()  # Filter by section
    context = {
        "faq_section": faq_section,
        "faqs": faqs,
    }
    return render(request, "FAQ.html", context)
