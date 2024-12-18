from django.db import models
from tinymce.models import HTMLField
from django.utils.translation import gettext_lazy as _

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