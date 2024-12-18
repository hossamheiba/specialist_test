from modeltranslation.translator import register, TranslationOptions
from .models import *



@register(FaqSection)
class FaqSectionTranslationOptions(TranslationOptions):
    fields = ('title', 'description' ) 
    
@register(FAQ)
class FAQTranslationOptions(TranslationOptions):
    fields = ('question', 'answer' ) 
    
