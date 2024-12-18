from django.db import models
from django.utils.translation import gettext_lazy as _
from Home.models import Headers

class PhotoGallery(models.Model):
    section = models.ForeignKey(Headers, on_delete=models.CASCADE)
    image = models.ImageField(_("Image"), upload_to="images/", blank=True, null=True)

    class Meta:
        verbose_name = _("Photo Gallery")
        verbose_name_plural = _("Photo Gallery")

    def __str__(self):
        return str(self.image.url) if self.image else _("No Image")



class PaymentMethod(models.Model):
    section = models.ForeignKey(Headers, on_delete=models.CASCADE)
    icon = models.ImageField(_("Icon"), upload_to="payment_methods/icons/", blank=True, null=True)

    class Meta:
        verbose_name = _("Payment Method")
        verbose_name_plural = _("Payment Methods")

    def __str__(self):
        return str(_("No icon"))
 
 

# Create your models here.
class ContactUs(models.Model):
    address = models.TextField(_("address"))  
    phone = models.PositiveIntegerField(_("phone"))
    email = models.EmailField(_("email"))
    
    def __str__(self):
        return f"Contact Us {self.address}"

    class Meta:
        verbose_name = _("Contact Us")
        verbose_name_plural = _("Contact Us")