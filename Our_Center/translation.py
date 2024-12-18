from modeltranslation.translator import register, TranslationOptions
from .models import *



@register(OurCenterSection)
class OurCenterSectionTranslationOptions(TranslationOptions):
    fields = ('first_section_title', 'first_section_description' ) 
    
@register(InformationOurCenter)
class InformationOurCenterTranslationOptions(TranslationOptions):
    fields = ('title','address' , 'working_days' , 'friday_status') 
    
@register(MapLocation)
class MapLocationTranslationOptions(TranslationOptions):
    fields = ('title','description','address') 
