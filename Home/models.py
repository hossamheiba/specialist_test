from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.html import mark_safe

# Headers ---------------------------------------------------
class Headers(models.Model):
    subtitle = models.CharField(_("Subtitle"), max_length=30, help_text=_("Maximum 30 characters"), blank=True, null=True)
    title = models.CharField(_("Title"), max_length=50, help_text=_("Maximum 50 characters"), blank=True, null=True)
    phone_number = models.CharField(_("Phone Number"), max_length=10, blank=True, null=True)
    video_link = models.URLField(_("Video Link"), blank=True, null=True)

    def __str__(self):
        return self.title or str (_("There Is No Title"))

    class Meta:
        verbose_name = _("1 - Header")
        verbose_name_plural = _("1 - Headers")


class BackgroundImage(models.Model):
    header = models.ForeignKey(Headers, related_name="background_images", on_delete=models.CASCADE)
    background_image = models.ImageField(
        _("Background Image"),
        upload_to="Home_Page/background_image/",
        help_text=mark_safe(_("Optional - If no image is uploaded, a default image will be used.")),
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.background_image) if self.background_image else _("No Background Image")

    class Meta:
        verbose_name = _("Background Image")
        verbose_name_plural = _("Background Images")


class FeatureItem(models.Model):
    header = models.ForeignKey(Headers, related_name="features", on_delete=models.CASCADE)
    icon_or_image = models.ImageField(_("Icon or Image"), upload_to="Home_Page/Feature_icon/",blank=True, null=True,)
    title = models.CharField(_("Title"), max_length=50, help_text=_("Maximum 50 characters"), blank=True, null=True)
    description = models.TextField(_("Description"), help_text=_("Maximum 100 characters"), blank=True, null=True)

    def __str__(self):
        return self.title or str (_("There Is No Title"))

    class Meta:
        verbose_name = _("Feature Item")
        verbose_name_plural = _("Feature Items")

# about home page -------------------------------------------
class AboutSection(models.Model):
    subtitle = models.CharField(_("subtitle"), max_length=50, help_text=_("Maximum characters 50"), blank=True)
    title = models.CharField(_("title"), max_length=40, help_text=_("Maximum characters 40"), blank=True)
    description = models.TextField(_("description"), help_text=_("Maximum characters 1000"), blank=True)
    image_1 = models.ImageField(_("image_1"), upload_to="Home_Page/About_Us/", blank=True, null=True)
    image_2 = models.ImageField(_("image_2"), upload_to="Home_Page/About_Us/", blank=True, null=True)

    counter_value = models.PositiveIntegerField(_("counter_value"), blank=True, null=True)
    counter_label = models.CharField(_("counter_label"), max_length=50, help_text=_("Maximum characters 50"), blank=True)
    counter_icon = models.ImageField(_("counter_icon"),upload_to="Home_Page/About_Us/",blank=True,null=True)
    
    experience_years = models.PositiveIntegerField(_("experience_years"), blank=True, null=True)
    experience_label = models.CharField(_("experience_label"), max_length=50, help_text=_("Maximum characters 50"), blank=True)
    experience_icon = models.ImageField(_("experience_icon"),upload_to="Home_Page/About_Us/",blank=True,null=True)

    class Meta:
        verbose_name = _("2 - About Section")
        verbose_name_plural = _("2 - About Sections")

    def __str__(self):
        return self.title or str (_("There Is No Title"))


#  WorkSection----------------------------------------------------
class WorkSection(models.Model):
    subtitle = models.CharField(_("subtitle"), max_length=30, help_text=_("Maximum characters 30"), blank=True,)
    title = models.CharField(_("title"), max_length=50, help_text=_("Maximum characters 50"), blank=True,)

    class Meta:
        verbose_name = _("3 - Work Section")
        verbose_name_plural = _("3 - Work Sections")

    def __str__(self):
        return self.title or str (_("There Is No Title"))

class WorkCard(models.Model):
    section = models.ForeignKey(WorkSection, related_name="cards", on_delete=models.CASCADE)
    title = models.CharField(_("title"), max_length=50, help_text=_("Maximum characters 50"), blank=True)
    description = models.TextField(_("Description") , max_length=1000 , help_text=_("Maximum characters 1000"), blank=True)
    icon = models.ImageField(_("Icon"), upload_to="Home_Page/work_card/" , blank=True, null=True ,)
    
    class Meta:
        verbose_name = _("Work Card")
        verbose_name_plural = _("Work Cards")

    def __str__(self):
        return self.title or str (_("There Is No Title"))


# services_page--------------------------------------------------------------------------------
class ServiceSection(models.Model):
    subtitle = models.CharField(_("subtitle"), max_length=50, help_text=_("Maximum characters 50"), blank=True, null=True)
    title = models.CharField(_("title"), max_length=50, help_text=_("Maximum characters 50"), blank=True, null=True)

    class Meta:
        verbose_name = _("4 - Service Section")
        verbose_name_plural = _("4 - Service Sections")

    def __str__(self):
        return self.title or str (_("There Is No Title"))


class ServiceCard(models.Model):
    PAGE_CHOICES = [
        ('mechanics', _("Mechanics")),
        ('electricity', _("Electricity")),
        ('bodywork_and_painting', _("Bodywork and Painting")),
        ('thermal_and_soundin_sulation', _("Thermal and Sound Insulation")),
        ('car_programming', _("Car Programming")),
        ('sports_suspension', _("Sports Suspension")),
        ('roadside_assistance', _("Roadside Assistance")),
    ]

    section = models.ForeignKey(ServiceSection, related_name="service_cards", on_delete=models.CASCADE)
    background_card = models.ImageField(_("background_card"), upload_to="work_card/icons/", blank=True, null=True)
    icon = models.ImageField(upload_to="Home_Page/Slider_Section/", blank=True, null=True)
    title = models.CharField(_("title"), max_length=30, help_text=_("Maximum characters 30"), blank=True, null=True, default="")
    page_type = models.CharField(max_length=50, choices=PAGE_CHOICES)

    class Meta:
        verbose_name = _("Service Card")
        verbose_name_plural = _("Service Cards")

    def __str__(self):
        return self.title or str (_("There Is No Title"))


# Slider_Section---------------------------------------------------------------------------- 
class SliderSection(models.Model):
    subtitle = models.CharField(_("subtitle"), max_length=30, help_text=_("Maximum characters 30"), blank=True, )
    title = models.CharField(_("title"), max_length=50, help_text=_("Maximum characters 50"), blank=True, )

    class Meta:
        verbose_name = _("5 - Slider Section")
        verbose_name_plural = _("5 - Slider Section")

    def __str__(self):
        return self.title or str (_("There Is No Title"))

class SliderCard(models.Model):
    section = models.ForeignKey(SliderSection, related_name="slider_card", on_delete=models.CASCADE)
    title = models.CharField(_("title"), max_length=50, help_text=_("Maximum characters 50"), blank=True, null=True)
    description = models.TextField(_("Description") , max_length=500 , help_text=_("Maximum characters 500"), blank=True, null=True)
    image = models.ImageField(_("image"), upload_to="Home_Page/Slider_Card/" , blank=True, null=True ,)
    
    class Meta:
        verbose_name = _("Slider Card")
        verbose_name_plural = _("Slider Cards")

    def __str__(self):
        return self.title or str (_("There Is No Title"))
    
    
    
# question and answer --------------------------------------------------------------------
class FAQSection(models.Model):
    subtitle = models.CharField(_("subtitle"), max_length=30, help_text=_("Maximum characters 30"), blank=True, null=True)
    title = models.CharField(_("title"), max_length=50, help_text=_("Maximum characters 50"), blank=True, null=True)
    image = models.ImageField(_("Image"), upload_to="Home_Page/FAQSection/", blank=True, null=True)
    
    def image_tag(self):
        if self.image:
            return mark_safe(
                f'<img src="{self.image.url}" width="50" height="50" '
                'style="border-radius: 10%; border: solid 1px #f26b3c;"/>'
            )
        return _("No Image")
    image_tag.short_description = _("Image ")

    class Meta:
        verbose_name = _("6 - FAQ Section")
        verbose_name_plural = _("6 - FAQ Sections")

    def __str__(self):
        return self.title or str (_("There Is No Title"))


class FAQItem(models.Model):
    section = models.ForeignKey(FAQSection, related_name="faq_items", on_delete=models.CASCADE,verbose_name=_("FAQ Section"))
    question = models.CharField(_("Question"), max_length=500, blank=True, null=True,help_text=_("Maximum characters 500"))
    answer = models.TextField(_("Answer"),max_length=5000, blank=True, null=True,help_text=_("Maximum characters 5000"))

    class Meta:
        verbose_name = _("FAQ Item")
        verbose_name_plural = _("FAQ Items")

    def __str__(self):
        return self.section.title or str (_("There Is No Title"))




# Why choose us ---------------------------------------------------------------------------- 
class ChooseUs(models.Model):
    subtitle = models.CharField(_("subtitle"), max_length=30, help_text=_("Maximum characters 30"), blank=True, null=True)
    title = models.CharField(_("title"), max_length=50, help_text=_("Maximum characters 50"), blank=True, null=True)

    class Meta:
        verbose_name = _("7 - ChooseUs Section")
        verbose_name_plural = _("7 - ChooseUs Section")

    def __str__(self):
        return self.title or str (_("There Is No Title"))

class ChooseUsCard(models.Model):
    section = models.ForeignKey(ChooseUs, related_name="choose_us_card", on_delete=models.CASCADE)
    icon = models.ImageField(_("Icon"), upload_to="Home_Page/Choose_Us/" , blank=True, null=True ,)
    title = models.CharField(_("title"), max_length=50, help_text=_("Maximum characters 50"), blank=True, null=True)
    description = models.TextField(_("Description") , max_length=500 , help_text=_("Maximum characters 500"), blank=True, null=True)
    
    class Meta:
        verbose_name = _("ChooseUs Card")
        verbose_name_plural = _("ChooseUs Cards")

    def __str__(self):
        return self.section.title or str (_("There Is No Title"))
    
    

#Brands ---------------------------------------------------------------------------- 
class Brands(models.Model):
    subtitle = models.CharField(_("subtitle"), max_length=30, help_text=_("Maximum characters 30"), blank=True, null=True)
    title = models.CharField(_("title"), max_length=50, help_text=_("Maximum characters 50"), blank=True, null=True)

    class Meta:
        verbose_name = _("8 - Brands Section")
        verbose_name_plural = _("8 - Brands Section")

    def __str__(self):
        return self.title or str (_("There Is No Title"))

class ImageBrand(models.Model):
    section = models.ForeignKey(Brands, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(_("image"), upload_to="Home_Page/Brands/" , blank=True, null=True ,)

    class Meta:
        verbose_name = _("ImageBrand Card")
        verbose_name_plural = _("ImageBrand Cards")

    def __str__(self):
        return self.section.title or str (_("There Is No Title"))
    
    
    
    
    
    
    


from Customers.models import User

class HomeComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="home_comments")
    comment = models.TextField(verbose_name="التعليق")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")

    class Meta:
        verbose_name = "تعليق"
        verbose_name_plural = "التعليقات"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}: {self.comment[:20]}"
