from Contact_Us.models import ContactUs

def loc_view(request):
    contact = ContactUs.objects.first()
    return {"contact" : contact}
