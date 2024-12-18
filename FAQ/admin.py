from django.contrib import admin
from .models import *
from modeltranslation.admin import  TranslationAdmin ,TranslationTabularInline ,TranslationStackedInline

#---------------------------------------------------1        
class FAQAdmin(TranslationStackedInline):
     model = FAQ
     extra = 1

@admin.register(FaqSection)
class FaqSectionAdmin(TranslationAdmin):
    inlines = [FAQAdmin]
    list_display = ('image_tag','title')
    list_display_links = ('image_tag','title') 


    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
        
        