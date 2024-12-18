from modeltranslation.translator import register, TranslationOptions
from .models import *



@register(JobInfo)
class OurCenterSectionTranslationOptions(TranslationOptions):
    fields = ('title',) 
    
