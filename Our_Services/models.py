from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.html import mark_safe
from tinymce.models import HTMLField


#--------------------------------------------------------------- 2
class Mechanics(models.Model):
    image_banner = models.ImageField(
        _("Image Banner"),
        upload_to='Our_Services/Mechanics/image_banner',
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
    first_section_description = HTMLField(_("First Section Description"), help_text=_("Description of the first section"), blank=True, null=True)
    first_section_image = models.ImageField(
        _("First Section Image"),
        upload_to="Our_Services/Mechanics/first_section_image",
        blank=True,
        null=True,
        help_text=mark_safe(_('recommended to use an image with a transparent background.'))
    )
    
    second_section_title = models.CharField(_("Second Section Title"), max_length=50, help_text=_("Maximum 50 characters"), blank=True, null=True)
    second_section_description = models.TextField(_("Second Section Description"), help_text=_("Description of the second section"), blank=True, null=True)
    second_section_image = models.ImageField(
        _("Second Section Image"),
        upload_to="Our_Services/Mechanics/second_section_image",
        blank=True,
        null=True,
        help_text=mark_safe(_('recommended to use an image with a transparent background.'))
    )
        
    def __str__(self):
      return self.first_section_title if self.first_section_title else str(_("No Title"))

        
    class Meta:
        verbose_name = _("1 - Mechanic")
        verbose_name_plural = _("1 - Mechanics")
    

class MechanicSlider(models.Model):
    mechanics = models.ForeignKey(
        Mechanics,
        related_name='sliders',
        on_delete=models.CASCADE,
        verbose_name=_("Mechanic")
    )
    slider_image = models.ImageField(
        _("Slider Image"),
        upload_to='Our_Services/Mechanics/slider_image',
        help_text=mark_safe(_('Optional - you can upload an image or leave it blank. <br> If no image is selected, a default image will be displayed.')),
        blank=True,
        null=True
    )
    
    def __str__(self):
        return f"{self.mechanics.first_section_title or _('No Title')} - Slider"
    
    class Meta:
        verbose_name = _("Mechanic Slider")
        verbose_name_plural = _("Mechanic Sliders")
        
        
        
#--------------------------------------------------------------- 2
class Electricity(models.Model):
    image_banner = models.ImageField(
        _("Image Banner"),
        upload_to='Our_Services/Electricity/image_banner',
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
    first_section_description = HTMLField(_("First Section Description"), help_text=_("Description of the first section"), blank=True, null=True)
    first_section_image = models.ImageField(
        _("First Section Image"),
        upload_to="Our_Services/Electricity/first_section_image/",
        blank=True,
        null=True,
        help_text=mark_safe(_('Optional - recommended to use an image with a transparent background.'))
    )
    
    second_section_title = models.CharField(_("Second Section Title"), max_length=50, help_text=_("Maximum 50 characters"), blank=True, null=True)
    second_section_description = models.TextField(_("Second Section Description"), help_text=_("Description of the second section"), blank=True, null=True)
    second_section_image = models.ImageField(
        _("Second Section Image"),
        upload_to="Our_Services/Electricity/second_section_image/",
        blank=True,
        null=True,
        help_text=mark_safe(_('Optional - recommended to use an image with a transparent background.'))
    )
        
    def __str__(self):
      return self.first_section_title.strip() if self.first_section_title else str(_("No Title"))

        
    class Meta:
        verbose_name = _("2 - Electricity")
        verbose_name_plural = _("2 - Electricity")
    

class ElectricitySlider(models.Model):
    electricity = models.ForeignKey(
        Electricity,
        related_name='sliders',
        on_delete=models.CASCADE,
        verbose_name=_("Electricity")
    )
    slider_image = models.ImageField(
        _("Slider Image"),
        upload_to='Our_Services/Electricity/slider_image',
        help_text=mark_safe(_('Optional - you can upload an image or leave it blank. <br> If no image is selected, a default image will be displayed.')),
        blank=True,
        null=True
    )
    
    def __str__(self):
        return f"{self.electricity.first_section_title or _('No Title')} - Slider"
    
    class Meta:
        verbose_name = _("electricity Slider")
        verbose_name_plural = _("electricity Sliders")
        
        
        
#--------------------------------------------------------------- 3
class BodyworkAndPainting(models.Model):
    image_banner = models.ImageField(
        _("Image Banner"),
        upload_to='Our_Services/Body_work_And_Painting/image_banner/',
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
    first_section_description = HTMLField(_("First Section Description"), help_text=_("Description of the first section"), blank=True, null=True)
    first_section_image = models.ImageField(
        _("First Section Image"),
        upload_to="Our_Services/Body_work_And_Painting/first_section_image/",
        blank=True,
        null=True,
        help_text=mark_safe(_('Optional - recommended to use an image with a transparent background.'))
    )
    
    second_section_title = models.CharField(_("Second Section Title"), max_length=50, help_text=_("Maximum 50 characters"), blank=True, null=True)
    second_section_description = models.TextField(_("Second Section Description"), help_text=_("Description of the second section"), blank=True, null=True)
    second_section_image = models.ImageField(
        _("Second Section Image"),
        upload_to="Our_Services/Body_work_And_Painting/second_section_image/",
        blank=True,
        null=True,
        help_text=mark_safe(_('Optional - recommended to use an image with a transparent background.'))
    )
        
    def __str__(self):
      return self.first_section_title.strip() if self.first_section_title else str(_("No Title"))

        
    class Meta:
        verbose_name = _("3 - BodyWork And Painting")
        verbose_name_plural = _("3 - BodyWork And Painting")
    

class BodyworkAndPaintingSlider(models.Model):
    bodyworkandpainting = models.ForeignKey(
        BodyworkAndPainting,
        related_name='sliders',
        on_delete=models.CASCADE,
        verbose_name=_("BodyworkAndPainting")
    )
    slider_image = models.ImageField(
        _("Slider Image"),
        upload_to='Our_Services/Body_work_And_Painting/slider_image/',
        help_text=mark_safe(_('Optional - you can upload an image or leave it blank. <br> If no image is selected, a default image will be displayed.')),
        blank=True,
        null=True
    )
    
    def __str__(self):
        return f"{self.bodyworkandpainting.first_section_title or _('No Title')} - Slider"
    
    class Meta:
        verbose_name = _("bodyworkandpainting Slider")
        verbose_name_plural = _("bodyworkandpainting Sliders")
        
        
#--------------------------------------------------------------- 4
class ThermalAndSoundInsulation(models.Model):
    image_banner = models.ImageField(
        _("Image Banner"),
        upload_to='Our_Services/Thermal_And_Sound_Insulation/image_banner/',
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
    first_section_description = HTMLField(_("First Section Description"), help_text=_("Description of the first section"), blank=True, null=True)
    first_section_image = models.ImageField(
        _("First Section Image"),
        upload_to="Our_Services/Thermal_And_Sound_Insulation/first_section_image/",
        blank=True,
        null=True,
        help_text=mark_safe(_('Optional - recommended to use an image with a transparent background.'))
    )
    
    second_section_title = models.CharField(_("Second Section Title"), max_length=50, help_text=_("Maximum 50 characters"), blank=True, null=True)
    second_section_description = models.TextField(_("Second Section Description"), help_text=_("Description of the second section"), blank=True, null=True)
    second_section_image = models.ImageField(
        _("Second Section Image"),
        upload_to="Our_Services/Thermal_And_Sound_Insulation/second_section_image/",
        blank=True,
        null=True,
        help_text=mark_safe(_('Optional - recommended to use an image with a transparent background.'))
    )
        
    def __str__(self):
      return self.first_section_title.strip() if self.first_section_title else str(_("No Title"))

        
    class Meta:
        verbose_name = _("4 - Thermal And Sound Insulation")
        verbose_name_plural = _("4 - Thermal And Sound Insulations")
    

class ThermalAndSoundInsulationSlider(models.Model):
    thermalandsoundinsulation = models.ForeignKey(
        ThermalAndSoundInsulation,
        related_name='sliders',
        on_delete=models.CASCADE,
        verbose_name=_("thermalandsoundinsulation")
    )
    slider_image = models.ImageField(
        _("Slider Image"),
        upload_to='Our_Services/Thermal_And_Sound_Insulation/slider_image/',
        help_text=mark_safe(_('Optional - you can upload an image or leave it blank. <br> If no image is selected, a default image will be displayed.')),
        blank=True,
        null=True
    )
    
    def __str__(self):
        return f"{self.thermalandsoundinsulation.first_section_title or _('No Title')} - Slider"
    
    class Meta:
        verbose_name = _("ThermalAndSoundInsulation Slider")
        verbose_name_plural = _("ThermalAndSoundInsulation Sliders")
        
        
        
        
#--------------------------------------------------------------- 5
class CarProgramming(models.Model):
    image_banner = models.ImageField(
        _("Image Banner"),
        upload_to='Our_Services/Car_Programming/image_banner/',
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
    first_section_description = HTMLField(_("First Section Description"), help_text=_("Description of the first section"), blank=True, null=True)
    first_section_image = models.ImageField(
        _("First Section Image"),
        upload_to="Our_Services/Car_Programming/first_section_image/",
        blank=True,
        null=True,
        help_text=mark_safe(_('Optional - recommended to use an image with a transparent background.'))
    )
    
    second_section_title = models.CharField(_("Second Section Title"), max_length=50, help_text=_("Maximum 50 characters"), blank=True, null=True)
    second_section_description = models.TextField(_("Second Section Description"), help_text=_("Description of the second section"), blank=True, null=True)
    second_section_image = models.ImageField(
        _("Second Section Image"),
        upload_to="Our_Services/Car_Programming/second_section_image/",
        blank=True,
        null=True,
        help_text=mark_safe(_('Optional - recommended to use an image with a transparent background.'))
    )
        
    def __str__(self):
      return self.first_section_title.strip() if self.first_section_title else str(_("No Title"))

        
    class Meta:
        verbose_name = _("5 - Car Programming")
        verbose_name_plural = _("5 - Car Programming")
    

class CarProgrammingSlider(models.Model):
    carprogramming = models.ForeignKey(
        CarProgramming,
        related_name='sliders',
        on_delete=models.CASCADE,
        verbose_name=_("carprogramming")
    )
    slider_image = models.ImageField(
        _("Slider Image"),
        upload_to='Our_Services/Car_Programming/slider_image/',
        help_text=mark_safe(_('Optional - you can upload an image or leave it blank. <br> If no image is selected, a default image will be displayed.')),
        blank=True,
        null=True
    )
    
    def __str__(self):
        return f"{self.carprogramming.first_section_title or _('No Title')} - Slider"
    
    class Meta:
        verbose_name = _("CarProgrammingSlider Slider")
        verbose_name_plural = _("CarProgrammingSlider Sliders")
        
        
        
        
#--------------------------------------------------------------- 6
class SportsSuspension(models.Model):
    image_banner = models.ImageField(
        _("Image Banner"),
        upload_to='Our_Services/Sports_Suspension/image_banner/',
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
    first_section_description = HTMLField(_("First Section Description"), help_text=_("Description of the first section"), blank=True, null=True)
    first_section_image = models.ImageField(
        _("First Section Image"),
        upload_to="Our_Services/Car_Programming/first_section_image/",
        blank=True,
        null=True,
        help_text=mark_safe(_('Optional - recommended to use an image with a transparent background.'))
    )
    
    second_section_title = models.CharField(_("Second Section Title"), max_length=50, help_text=_("Maximum 50 characters"), blank=True, null=True)
    second_section_description = models.TextField(_("Second Section Description"), help_text=_("Description of the second section"), blank=True, null=True)
    second_section_image = models.ImageField(
        _("Second Section Image"),
        upload_to="Our_Services/Car_Programming/second_section_image/",
        blank=True,
        null=True,
        help_text=mark_safe(_('Optional - recommended to use an image with a transparent background.'))
    )
        
    def __str__(self):
      return self.first_section_title.strip() if self.first_section_title else str(_("No Title"))

        
    class Meta:
        verbose_name = _("6 - Sports Suspension")
        verbose_name_plural = _("6 - Sports Suspension")
    

class SportsSuspensionSlider(models.Model):
    sportssuspension = models.ForeignKey(
        SportsSuspension,
        related_name='sliders',
        on_delete=models.CASCADE,
        verbose_name=_("sportssuspension")
    )
    slider_image = models.ImageField(
        _("Slider Image"),
        upload_to='Our_Services/Car_Programming/slider_image/',
        help_text=mark_safe(_('Optional - you can upload an image or leave it blank. <br> If no image is selected, a default image will be displayed.')),
        blank=True,
        null=True
    )
    
    def __str__(self):
        return f"{self.sportssuspension.first_section_title or _('No Title')} - Slider"
    
    class Meta:
        verbose_name = _("SportsSuspensionSlider Slider")
        verbose_name_plural = _("SportsSuspensionSlider Sliders")
        
        
        
        
#--------------------------------------------------------------- 7
class RoadsideAssistance(models.Model):
    image_banner = models.ImageField(
        _("Image Banner"),
        upload_to='Our_Services/Roadside_Assistance/image_banner/',
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
    first_section_description = HTMLField(_("First Section Description"), help_text=_("Description of the first section"), blank=True, null=True)
    first_section_image = models.ImageField(
        _("First Section Image"),
        upload_to="Our_Services/Roadside_Assistance/first_section_image/",
        blank=True,
        null=True,
        help_text=mark_safe(_('Optional - recommended to use an image with a transparent background.'))
    )
    
    second_section_title = models.CharField(_("Second Section Title"), max_length=50, help_text=_("Maximum 50 characters"), blank=True, null=True)
    second_section_description = models.TextField(_("Second Section Description"), help_text=_("Description of the second section"), blank=True, null=True)
    second_section_image = models.ImageField(
        _("Second Section Image"),
        upload_to="Our_Services/Roadside_Assistance/second_section_image/",
        blank=True,
        null=True,
        help_text=mark_safe(_('Optional - recommended to use an image with a transparent background.'))
    )
        
    def __str__(self):
      return self.first_section_title.strip() if self.first_section_title else str(_("No Title"))

        
    class Meta:
        verbose_name = _("7 - Roadside Assistance")
        verbose_name_plural = _("7 - Roadside Assistance")
    

class RoadsideAssistanceSlider(models.Model):
    roadsideassistance = models.ForeignKey(
        RoadsideAssistance,
        related_name='sliders',
        on_delete=models.CASCADE,
        verbose_name=_("roadsideassistance")
    )
    slider_image = models.ImageField(
        _("Slider Image"),
        upload_to='Our_Services/Roadside_Assistance/slider_image/',
        help_text=mark_safe(_('Optional - you can upload an image or leave it blank. <br> If no image is selected, a default image will be displayed.')),
        blank=True,
        null=True
    )
    
    def __str__(self):
        return f"{self.roadsideassistance.first_section_title or _('No Title')} - Slider"
    
    class Meta:
        verbose_name = _("RoadsideAssistanceSlider Slider")
        verbose_name_plural = _("RoadsideAssistanceSlider Sliders")
