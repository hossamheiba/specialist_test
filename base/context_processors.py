from .models import PhotoGallery , PaymentMethod , ContactUs

def photo_gallery_view_context(request):
    images = PhotoGallery.objects.all()
    return {
        "images": images,
    }


def payment_methods_view(request):
    payment_methods = PaymentMethod.objects.all()
    return {
        "payment_methods": payment_methods,
    }
    
    
def contactus(request):
    contact = ContactUs.objects.first()
    return {
        "contact": contact,
    }
