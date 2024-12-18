from modeltranslation.translator import register, TranslationOptions
from .models import *

# Headers ---------------------------------------------------
@register(Headers)
class HeadersTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle') 
    
@register(FeatureItem)
class FeatureItemTranslationOptions(TranslationOptions):
    fields = ('title', 'description') 
    

# AboutSection ---------------------------------------------------
@register(AboutSection)
class AboutSectionTranslationOptions(TranslationOptions):
    fields = ( 'subtitle','title','description','counter_label', 'experience_label') 
    
    
    
# WorkSection------------------------------------------------
@register(WorkSection)
class WorkSectionTranslationOptions(TranslationOptions):
    fields = ( 'subtitle','title') 
    

@register(WorkCard)
class WorkCardTranslationOptions(TranslationOptions):
    fields = ('title' , 'description') 
    

# ServiceSection ----------------------------------------------------------
@register(ServiceSection)
class ServiceSectionTranslationOptions(TranslationOptions):
    fields = ( 'subtitle','title') 
    

@register(ServiceCard)
class ServiceCardTranslationOptions(TranslationOptions):
    fields = ('title',) 
    



# SliderSection ---------------------------------------------------------
@register(SliderSection)
class SliderSectionTranslationOptions(TranslationOptions):
    fields = ( 'subtitle','title') 
    


@register(SliderCard)
class SliderCardTranslationOptions(TranslationOptions):
    fields = ('title' , 'description') 
    


# FAQSection ---------------------------------------------------------
@register(FAQSection)
class FAQSectionSectionTranslationOptions(TranslationOptions):
    fields = ( 'subtitle','title') 
    

@register(FAQItem)
class FAQItemTranslationOptions(TranslationOptions):
    fields = ('question' , 'answer') 
    


# Why choose us? ---------------------------------------------------------
@register(ChooseUs)
class ChooseUsTranslationOptions(TranslationOptions):
    fields = ('subtitle','title') 
    

@register(ChooseUsCard)
class ChooseUsCardTranslationOptions(TranslationOptions):
    fields = ('title' , 'description') 
    

# Brands---------------------------------------------------------
@register(Brands)
class BrandsTranslationOptions(TranslationOptions):
    fields = ( 'subtitle','title') 
    
