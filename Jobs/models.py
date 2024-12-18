from django.db import models

from django.utils.translation import gettext_lazy as _
from django.utils.html import mark_safe


class JobInfo(models.Model):
    image_banner = models.ImageField(
        _("Image Banner"),
        upload_to='Our_Services/Electricity/image_banner/',
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
    
    title = models.CharField(_("Title"), max_length=50, help_text=_("Maximum 50 characters"), blank=True, null=True)
    image = models.ImageField(
        _("First Section Image"),
        upload_to="Our_Services/Electricity/first_section_image/",
        blank=True,
        null=True,
    )
    

        
    def __str__(self):
      return self.title.strip() if self.title else str(_("No Title"))

        
    class Meta:
        verbose_name = _("Job Info")
        verbose_name_plural = _("Job Info")
    
    
class JobApplication(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    job_title = models.CharField(max_length=255)
    experience_years = models.PositiveIntegerField()
    resume = models.FileField(upload_to='resumes/')
    portfolio = models.FileField(upload_to='portfolios/', null=True, blank=True)
    about = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Application from {self.name}"
