from django.contrib.auth.decorators import login_required
from .models import HomeComment
from django.shortcuts import render , redirect
from .models import *

def home_section_view(request):
    header = Headers.objects.prefetch_related("background_images")
    feature_items = FeatureItem.objects.all() 
    about_sections = AboutSection.objects.all()
    section = WorkSection.objects.prefetch_related('cards').first()
    services = ServiceSection.objects.prefetch_related('service_cards').first()
    slider_section  = SliderSection.objects.prefetch_related('slider_card').first()
    faq_section = FAQSection.objects.prefetch_related("faq_items").first()  
    choose_us = ChooseUs.objects.prefetch_related("choose_us_card").first()  
    brand = Brands.objects.prefetch_related("images").first()  
    comments = HomeComment.objects.all() 
    
    user_has_commented = False
    if request.user.is_authenticated:
        user_has_commented = HomeComment.objects.filter(user=request.user).exists()

    context = {
        "header": header,
         "feature_items": feature_items,
         "about_sections": about_sections, 
         "section": section,
         "services": services,
         "slider_section": slider_section,
         "faq_section": faq_section,
         "choose_us": choose_us,
         "brand": brand,
         'comments': comments ,
         'user_has_commented': user_has_commented
        }
     
    return render(request, "Home.html", context)





@login_required
def add_comment(request):
    if request.method == "POST":
        comment_text = request.POST.get('comment')
        if not HomeComment.objects.filter(user=request.user).exists():
            HomeComment.objects.create(user=request.user, comment=comment_text)
        return redirect('/')
