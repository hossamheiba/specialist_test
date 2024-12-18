from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline
from base.models import PhotoGallery , PaymentMethod


# Headers------------------------------------------------------------
class PaymentMethodInline(admin.StackedInline):  
    model = PaymentMethod
    extra = 1
    
class PhotoGalleryInline(admin.StackedInline):  
    model = PhotoGallery
    extra = 1
    
class BackgroundImageInline(admin.StackedInline):  
    model = BackgroundImage
    extra = 1
    
class FeatureItemInline(TranslationStackedInline):  
    model = FeatureItem
    max_num = 3  

@admin.register(Headers)
class HeadersAdmin(TranslationAdmin):
    list_display = ("title", "subtitle", "phone_number")  
    search_fields = ("subtitle","title",)
    list_filter = ("subtitle","title",)
    inlines = [BackgroundImageInline , FeatureItemInline , PhotoGalleryInline , PaymentMethodInline]  
    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
        
        
        
# AboutSection------------------------------------------------------------------
@admin.register(AboutSection)
class AboutSectionAdmin(TranslationAdmin):
    list_display = ("title", "counter_value", "experience_years")

    
    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }




# WorkSection-------------------------------------------------------------
class WorkCardInline(TranslationStackedInline):
    model = WorkCard
    max_num = 3  

@admin.register(WorkSection)
class WorkSectionAdmin(TranslationAdmin):
    list_display = ("title", "subtitle")
    inlines = [WorkCardInline]
    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
        
        
        
        
# ServiceSection-------------------------------------------------------------
class ServiceCardInline(TranslationStackedInline):
    model = ServiceCard
    max_num = 7  


@admin.register(ServiceSection)
class ServiceSectionAdmin(TranslationAdmin):
    list_display = ("title", "subtitle")
    inlines = [ServiceCardInline]
    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }



# SliderSection-------------------------------------------------------------
class SliderCardInline(TranslationStackedInline):
    model =  SliderCard
    extra = 1


@admin.register(SliderSection)
class SliderSectionAdmin(TranslationAdmin):
    list_display = ("title", "subtitle")
    inlines = [SliderCardInline]
    
    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
        
        
        

# SliderSection-------------------------------------------------------------
class FAQItemCardInline(TranslationStackedInline):
    model =  FAQItem
    extra = 1


@admin.register(FAQSection)
class FAQSectionAdmin(TranslationAdmin):
    list_display = ("image_tag", "title", "subtitle")
    inlines = [FAQItemCardInline]
    
    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
        
        
        
        
# Why choose us?-------------------------------------------------------------
class ChooseUsCardInline(TranslationStackedInline):
    model =  ChooseUsCard
    extra = 1


@admin.register(ChooseUs)
class ChooseUsAdmin(TranslationAdmin):
    list_display = ("title", "subtitle")
    inlines = [ChooseUsCardInline]
    
    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
        
        
        
# Brands------------------------------------------------------------
class ImageBrandInline(admin.StackedInline):  
    model = ImageBrand
    extra = 1

@admin.register(Brands)
class BrandsAdmin(TranslationAdmin):
    list_display = ("subtitle","title",)
    inlines = [ImageBrandInline]  
    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
                







@admin.register(HomeComment)
class HomeCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment', 'created_at')
    list_display_links = ('comment',)  
    list_filter = ('created_at',)
    search_fields = ('user__first_name', 'user__last_name', 'comment')
    readonly_fields = ('comment',)

