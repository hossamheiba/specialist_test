from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.html import mark_safe

class NewsSliderSection(models.Model):
    image_banner = models.ImageField(
        _("Image Banner"),
        upload_to='NewsSliderSection/image_banner/',
        help_text=mark_safe(_('Optional - you can upload an image or leave it blank. <br> If no image is selected, a default image will be displayed.')),
        blank=True,
        null=True
    )
    title = models.CharField(_("title"), max_length=50, help_text=_("Maximum characters 50"), blank=True, null=True)
    
    
    
    def image_tag(self):
        if self.image_banner:
            return mark_safe(
                f'<img src="{self.image_banner.url}" width="50" height="50" '
                'style="border-radius: 10%; border: solid 1px #f26b3c;"/>'
            )
        return _("No Image")
    image_tag.short_description = _("Image Banner")
    
    
    class Meta:
        verbose_name = _("news Slider")
        verbose_name_plural = _(" news  Selider")

    def __str__(self):
        return self.title if self.title else str (_("There Is No Title"))


class NewsSlider(models.Model):
    slider = models.ForeignKey(NewsSliderSection, related_name="news_sliders", on_delete=models.CASCADE, )
    image = models.ImageField(_("image"), upload_to="NewsSliderSection/icons/" , blank=True, null=True )



    class Meta:
        verbose_name = _("news Selider")
        verbose_name_plural = _("news Selider")

    def __str__(self):
        return self.slider.title if self.slider.title else  str (_("There Is No Title"))





#------------------------------------------------------------------
class NewsSection(models.Model):
    title = models.CharField(_("title"), max_length=50, help_text=_("Maximum characters 50"), blank=True, null=True)

    class Meta:
        verbose_name = _("news Section")
        verbose_name_plural = _(" news Sections")

    def __str__(self):
        return self.title if self.title else "There Is No Title"


class NewsCard(models.Model):
    offer = models.ForeignKey(NewsSection, related_name="news_cards", on_delete=models.CASCADE, )
    background_card = models.ImageField(_("background_card"), upload_to="work_card/icons/" , blank=True, null=True )
    title = models.CharField(_("title"), max_length=30, help_text=_("Maximum characters 30"), blank=True, null=True)
    content = models.CharField(_("content"), max_length=100, help_text=_("Maximum characters 100"), blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    


    class Meta:
        verbose_name = _("news Card")
        verbose_name_plural = _("news Cards")

    def __str__(self):
        return self.title if self.title else "There Is No Title"


