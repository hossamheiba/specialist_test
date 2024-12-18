from modeltranslation.translator import register, TranslationOptions
from .models import AboutSection

# Headers ---------------------------------------------------
@register(AboutSection)
class AboutSectionTranslationOptions(TranslationOptions):
    fields = ('sub_title', 'vision_title' , 'vision_text' , 'goals_title' , 'goals_list' , 'why_us_title' , 'why_us_points') 
    
