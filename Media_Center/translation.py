from modeltranslation.translator import register, TranslationOptions
from .models import *



@register(NewsSliderSection)
class NewsSliderSectionTranslationOptions(TranslationOptions):
    fields = ('title',) 
    

@register(NewsSection)
class NewsSectionTranslationOptions(TranslationOptions):
    fields = ('title',) 
    
@register(NewsCard)
class NewsCardTranslationOptions(TranslationOptions):
    fields = ('title' , 'content' ,) 
    