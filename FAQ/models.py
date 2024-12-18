from django.db import models
from django.utils.html import mark_safe
from django.utils.translation import gettext_lazy as _


class FaqSection(models.Model):
    image_banner = models.ImageField(
        _("Image Banner"),
        upload_to='FaqSection/image_banner/',
        help_text=mark_safe(_('Optional - you can upload an image or leave it blank. <br> If no image is selected, a default image will be displayed.')),
        blank=True,
        null=True
    )
    title = models.CharField(_("Section Title"), max_length=50, help_text=_("Maximum 50 characters"), blank=True, null=True)
    description = models.TextField(_("Description"), help_text=_("Description of the first section"), blank=True, null=True)
    image = models.ImageField(
        _("First Section Image"),
        upload_to="FaqSection/first_section_image/",
        blank=True,
        null=True,
        help_text=mark_safe(_('Optional - recommended to use an image with a transparent background.'))
    )

    def image_tag(self):
        if self.image_banner:
            return mark_safe(
                f'<img src="{self.image_banner.url}" width="50" height="50" '
                'style="border-radius: 10%; border: solid 1px #f26b3c;"/>'
            )
        return _("No Image")
    image_tag.short_description = _("Image Banner")

    def __str__(self):
        return self.title if self.title else str(_("No Title"))

    class Meta:
        verbose_name = _("FAQ Section")
        verbose_name_plural = _("FAQ Sections")


class FAQ(models.Model):
    faq_section = models.ForeignKey(
        FaqSection,
        related_name='faqs',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    question = models.TextField(_("Question"), blank=True, null=True)
    answer = models.TextField(_("Answer"), blank=True, null=True)

    def __str__(self):
        return self.question if self.question else str(_("No Question Provided"))

    class Meta:
        verbose_name = _("FAQ")
        verbose_name_plural = _("FAQs")
