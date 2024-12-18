from django.contrib import admin
from .models import AboutSection
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline




@admin.register(AboutSection)
class AboutSectionAdmin(TranslationAdmin):
    list_display = ("sub_title","vision_title",'goals_title' , 'why_us_title')
    search_fields = ('sub_title', 'vision_title', 'goals_title')
    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
                