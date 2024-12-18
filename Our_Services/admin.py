from django.contrib import admin
from .models import *
from modeltranslation.admin import  TranslationAdmin ,TranslationTabularInline ,TranslationStackedInline

# Mechanics ---------------------------------------------------
class MechanicSliderAdmin(admin.StackedInline):
     model = MechanicSlider
     extra = 1

@admin.register(Mechanics)
class MechanicsAdmin(TranslationAdmin):
    inlines = [MechanicSliderAdmin]
    list_display = ('image_tag','first_section_title' , 'second_section_title' )
    list_display_links = ('image_tag','first_section_title' , 'second_section_title' ) 


    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
        
        

# Electricity --------------------------------------------------    
        
class ElectricitySliderAdmin(admin.StackedInline):
     model = ElectricitySlider
     extra = 1

@admin.register(Electricity)
class ElectricityAdmin(TranslationAdmin):
    inlines = [ElectricitySliderAdmin]
    list_display = ('image_tag','first_section_title' , 'second_section_title' )
    list_display_links = ('image_tag','first_section_title' , 'second_section_title' ) 


    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
        
        
        
# BodyworkAndPainting ---------------------------------------------------        
class BodyworkAndPaintingSliderAdmin(admin.StackedInline):
     model = BodyworkAndPaintingSlider
     extra = 1

@admin.register(BodyworkAndPainting)
class BodyworkAndPaintingAdmin(TranslationAdmin):
    inlines = [BodyworkAndPaintingSliderAdmin]
    list_display = ('image_tag','first_section_title' , 'second_section_title' )
    list_display_links = ('image_tag','first_section_title' , 'second_section_title' ) 

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
        
        
        
        
# ThermalAndSoundInsulation ---------------------------------------------------   
class ThermalAndSoundInsulationSliderAdmin(admin.StackedInline):
     model = ThermalAndSoundInsulationSlider
     extra = 1

@admin.register(ThermalAndSoundInsulation)
class ThermalAndSoundInsulationAdmin(TranslationAdmin):
    inlines = [ThermalAndSoundInsulationSliderAdmin]
    list_display = ('image_tag','first_section_title' , 'second_section_title' )
    list_display_links = ('image_tag','first_section_title' , 'second_section_title' ) 

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
        
        
        
        
# CarProgramming ---------------------------------------------------  
class CarProgrammingSliderAdmin(admin.StackedInline):
     model = CarProgrammingSlider
     extra = 1

@admin.register(CarProgramming)
class CarProgrammingAdmin(TranslationAdmin):
    inlines = [CarProgrammingSliderAdmin]
    list_display = ('image_tag','first_section_title' , 'second_section_title' )
    list_display_links = ('image_tag','first_section_title' , 'second_section_title' ) 

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
        
        
        
        
# SportsSuspension ---------------------------------------------------
class SportsSuspensionSliderAdmin(admin.StackedInline):
     model = SportsSuspensionSlider
     extra = 1

@admin.register(SportsSuspension)
class SportsSuspensionAdmin(TranslationAdmin):
    inlines = [SportsSuspensionSliderAdmin]
    list_display = ('image_tag','first_section_title' , 'second_section_title' )
    list_display_links = ('image_tag','first_section_title' , 'second_section_title' ) 

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
        
        
        
        
        
# RoadsideAssistance ---------------------------------------------------
class RoadsideAssistanceSliderAdmin(admin.StackedInline):
     model = RoadsideAssistanceSlider
     extra = 1

@admin.register(RoadsideAssistance)
class RoadsideAssistanceSliderAdmin(TranslationAdmin):
    inlines = [RoadsideAssistanceSliderAdmin]
    list_display = ('image_tag','first_section_title' , 'second_section_title' )
    list_display_links = ('image_tag','first_section_title' , 'second_section_title' ) 


    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
        
