from modeltranslation.translator import register, TranslationOptions
from .models import *



@register(OfferSliderSection)
class MechanicsTranslationOptions(TranslationOptions):
    fields = ('title','description',) 
    



@register(OfferSection)
class MechanicsTranslationOptions(TranslationOptions):
    fields = ('title',) 
    
@register(OfferCard)
class MechanicsTranslationOptions(TranslationOptions):
    fields = ('title' , 'content_one' , 'content_tow') 
    