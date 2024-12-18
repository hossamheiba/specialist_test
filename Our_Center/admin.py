from django.contrib import admin
from .models import *
from modeltranslation.admin import  TranslationAdmin ,TranslationTabularInline ,TranslationStackedInline


@admin.register(OurCenterSection)
class OurCenterSectionAdmin(TranslationAdmin):
    list_display = ('image_tag','first_section_title' )
    list_display_links = ('first_section_title', ) 


    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
        




class MapLocationAdmin(TranslationStackedInline):
     model = MapLocation
     extra = 1

@admin.register(InformationOurCenter)
class InformationOurCenterAdmin(TranslationAdmin):
    list_display = ('title', 'working_hours', 'working_days', 'friday_status')
    search_fields = ('title', 'address')
    inlines = [MapLocationAdmin]


    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
        







