from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.html import mark_safe

class OfferSliderSection(models.Model):
    image_banner = models.ImageField(
        _("Image Banner"),
        upload_to='OfferSliderSection/image_banner/',
        help_text=mark_safe(_('Optional - you can upload an image or leave it blank. <br> If no image is selected, a default image will be displayed.')),
        blank=True,
        null=True
    )
    
    title = models.CharField(_("title"), max_length=50, help_text=_("Maximum characters 50"), blank=True, null=True)
    description = models.TextField(_("Description"), max_length=1000, help_text=_("Maximum characters 1000"),blank=True, null=True)
    
    
    def image_tag(self):
        if self.image_banner:
            return mark_safe(
                f'<img src="{self.image_banner.url}" width="50" height="50" '
                'style="border-radius: 10%; border: solid 1px #f26b3c;"/>'
            )
        return _("No Image")
    image_tag.short_description = _("Image Banner")
    
    
    class Meta:
        verbose_name = _("offer Slider")
        verbose_name_plural = _(" offer  Selider")

    def __str__(self):
        return self.title if self.title else str (_("There Is No Title"))


class OfferSlider(models.Model):
    slider = models.ForeignKey(OfferSliderSection, related_name="offer_sliders", on_delete=models.CASCADE, )
    image = models.ImageField(_("image"), upload_to="OfferSliderSection/icons/" , blank=True, null=True )



    class Meta:
        verbose_name = _("offer Selider")
        verbose_name_plural = _("offer Selider")

    def __str__(self):
        return self.slider.title if self.slider.title else str (_("There Is No Title"))



#------------------------------------------------------------------
class OfferSection(models.Model):
    title = models.CharField(_("title"), max_length=50, help_text=_("Maximum characters 50"), blank=True, null=True)

    class Meta:
        verbose_name = _("offer Section")
        verbose_name_plural = _(" Sections")

    def __str__(self):
        return self.title if self.title else str (_("There Is No Title"))


class OfferCard(models.Model):
    
    PAGE_CHOICES = [
        ('mechanics', _("Mechanics")),
        ('electricity', _("Electricity")),
        ('bodywork_and_painting', _("Bodywork_And_Pinting")),
        ('thermal_and_soundin_sulation', _("Thermal_And_Soundin_Sulation")),
        ('car_programming', _("Car_Programming")),
        ('sports_suspension', _("Sports_Suspension")),
        ('roadside_assistance', _("Roadside_Assistance")),
    ]

    offer = models.ForeignKey(OfferSection, related_name="offer_cards", on_delete=models.CASCADE, )
    background_card = models.ImageField(_("background_card"), upload_to="work_card/icons/" , blank=True, null=True )
    title = models.CharField(_("title"), max_length=30, help_text=_("Maximum characters 30"), blank=True, null=True)
    content_one = models.CharField(_("content_one"), max_length=100, help_text=_("Maximum characters 100"), blank=True, null=True)
    content_tow = models.CharField(_("content_tow"), max_length=100, help_text=_("Maximum characters 100"), blank=True, null=True)
    page_type = models.CharField(max_length=100, choices=PAGE_CHOICES, )
    


    class Meta:
        verbose_name = _("offer Card")
        verbose_name_plural = _("offer Cards")

    def __str__(self):
        return self.title if self.title else str (_("There Is No Title"))


