from django.contrib import admin
from django.contrib import admin
from .models import *
from modeltranslation.admin import  TranslationAdmin ,TranslationTabularInline ,TranslationStackedInline




class OfferSliderAdmin(admin.StackedInline):
     model = OfferSlider
     extra = 1

@admin.register(OfferSliderSection)
class OfferSliderSectionAdmin(TranslationAdmin):
    inlines = [OfferSliderAdmin]
    list_display = ('image_tag','title', )
    list_display_links = ('title',) 


    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
        
        
        



# -----------------------------------------------
class OfferCardAdmin(TranslationStackedInline):
     model = OfferCard
     extra = 1

@admin.register(OfferSection)
class OfferSectionAdmin(TranslationAdmin):
    inlines = [OfferCardAdmin]
    list_display = ('title', )
    list_display_links = ('title',) 


    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
        
        
        