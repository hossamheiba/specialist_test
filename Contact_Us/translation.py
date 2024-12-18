from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(ContactUs)
class ContactUsTranslationOptions(TranslationOptions):
    fields = ('address',) 
