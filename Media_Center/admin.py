from django.contrib import admin
from django.contrib import admin
from .models import *
from modeltranslation.admin import  TranslationAdmin ,TranslationTabularInline ,TranslationStackedInline




class NewsSliderSliderAdmin(admin.StackedInline):
     model = NewsSlider
     extra = 1

@admin.register(NewsSliderSection)
class NewsSliderSectionAdmin(TranslationAdmin):
    inlines = [NewsSliderSliderAdmin]
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
class NewsCardAdmin(TranslationStackedInline):
     model = NewsCard
     extra = 1

@admin.register(NewsSection)
class NewsSectionAdmin(TranslationAdmin):
    inlines = [NewsCardAdmin]
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
        
        
        