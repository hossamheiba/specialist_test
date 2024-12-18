from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext_lazy as _
from django.utils.html import mark_safe


class OurCenterSection(models.Model):
    image_banner = models.ImageField(
        _("Image Banner"),
        upload_to='OurCenterSection/image_banner/',
        help_text=mark_safe(_('Optional - you can upload an image or leave it blank. <br> If no image is selected, a default image will be displayed.')),
        blank=True,
        null=True
    )
    
    def image_tag(self):
        if self.image_banner:
            return mark_safe(
                f'<img src="{self.image_banner.url}" width="50" height="50" '
                'style="border-radius: 10%; border: solid 1px #f26b3c;"/>'
            )
        return _("No Image")
    image_tag.short_description = _("Image Banner")
    
    first_section_title = models.CharField(_("First Section Title"), max_length=50, help_text=_("Maximum 50 characters"), blank=True, null=True)
    first_section_description = models.TextField(_("First Section Description"), help_text=_("Description of the first section"), blank=True, null=True)
    first_section_image = models.ImageField(
        _("First Section Image"),
        upload_to="OurCenterSection/first_section_image/",
        blank=True,
        null=True,
        help_text=mark_safe(_('Optional - recommended to use an image with a transparent background.'))
    )

    class Meta:
        verbose_name = _("OurCenter Section")
        verbose_name_plural = _("OurCenter Sections")

    def __str__(self):
        return self.first_section_title or str(_("Unnamed Location")
)





class InformationOurCenter(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("Center Title"))
    address = models.TextField(null=True, blank=True, verbose_name=_("Address"))
    working_hours = models.CharField(max_length=50, null=True, blank=True, verbose_name=_("Working Hours"))
    working_days = models.CharField(max_length=50, null=True, blank=True, verbose_name=_("Working Days"))
    friday_status = models.CharField(max_length=50, null=True, blank=True, verbose_name=_("Friday Status"))

    class Meta:
        verbose_name = _("Information Our Center")
        verbose_name_plural = _("Information Our Center ")

    def __str__(self):
        return self.title or str(_("Center without Title"))




class MapLocation(models.Model):
    section = models.ForeignKey(InformationOurCenter,on_delete=models.CASCADE,verbose_name=_("map"))
    title = models.CharField(max_length=255, verbose_name=_("Title"), null=True, blank=True)
    description = models.TextField(verbose_name=_("Description"), null=True, blank=True)
    latitude = models.FloatField(verbose_name=_("Latitude"))
    longitude = models.FloatField(verbose_name=_("Longitude"))
    address = models.CharField(max_length=255, verbose_name=_("Address"), null=True, blank=True)
    image = models.ImageField(upload_to="map/images/", verbose_name=_("Image"), null=True, blank=True)
    url = models.URLField(verbose_name=_("Google Maps URL"), null=True, blank=True)

    class Meta:
        verbose_name = _("Map Location")
        verbose_name_plural = _("Map Locations")

    def __str__(self):
        return self.title or str(_("Unnamed Location"))
