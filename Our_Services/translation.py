from modeltranslation.translator import register, TranslationOptions
from .models import *



@register(Mechanics)
class MechanicsTranslationOptions(TranslationOptions):
    fields = ('first_section_title', 'first_section_description' , 'second_section_title' , 'second_section_description') 
    
@register(Electricity)
class ElectricityTranslationOptions(TranslationOptions):
    fields = ('first_section_title', 'first_section_description' , 'second_section_title' , 'second_section_description') 
    
@register(BodyworkAndPainting)
class BodyworkAndPaintingTranslationOptions(TranslationOptions):
    fields = ('first_section_title', 'first_section_description' , 'second_section_title' , 'second_section_description') 
    
@register(ThermalAndSoundInsulation)
class ThermalAndSoundInsulationTranslationOptions(TranslationOptions):
    fields = ('first_section_title', 'first_section_description' , 'second_section_title' , 'second_section_description') 
    
@register(CarProgramming)
class CarProgrammingTranslationOptions(TranslationOptions):
    fields = ('first_section_title', 'first_section_description' , 'second_section_title' , 'second_section_description') 
    
    
@register(SportsSuspension)
class SportsSuspensionTranslationOptions(TranslationOptions):
    fields = ('first_section_title', 'first_section_description' , 'second_section_title' , 'second_section_description') 
    
    
@register(RoadsideAssistance)
class RoadsideAssistanceTranslationOptions(TranslationOptions):
    fields = ('first_section_title', 'first_section_description' , 'second_section_title' , 'second_section_description') 
    
