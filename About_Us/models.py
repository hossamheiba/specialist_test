from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.html import mark_safe



class AboutSection(models.Model):
    image_banner = models.ImageField(
        _("Image Banner"),
        upload_to='AboutSection/image_banner/',
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
    


    sub_title = models.CharField(max_length=40, null=True, blank=True,help_text=_("Maximum 40 characters"), verbose_name=_("Subtitle"))
    vision_title = models.CharField(max_length=50, null=True, blank=True,help_text=_("Maximum 50 characters"), verbose_name=_("Vision Title"))
    vision_text = models.TextField(null=True, blank=True, verbose_name=_("Vision Text"))
    goals_title = models.CharField(max_length=50, null=True, blank=True, help_text=_("Maximum 50 characters"),verbose_name=_("Goals Title"))
    goals_list = models.TextField(null=True, blank=True, verbose_name=_("Goals List (each goal in a line)"))
    why_us_title = models.CharField(max_length=50, null=True, blank=True, help_text=_("Maximum 50 characters"),verbose_name=_("Why Us Title"))
    why_us_points = models.TextField(null=True, blank=True, verbose_name=_("Why Us Points (each point in a line)"))
    first_image = models.ImageField(upload_to="AboutSection/images/", null=True, blank=True, verbose_name=_("Main Image"))
    second_image = models.ImageField(upload_to="AboutSection/images/", null=True, blank=True, verbose_name=_("second_image"))

    class Meta:
        verbose_name = _("About Section")
        verbose_name_plural = _("About Sections")

    def __str__(self):
        return self.sub_title or str (_("New About Section"))