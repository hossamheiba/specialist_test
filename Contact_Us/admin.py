from django.contrib import admin
from modeltranslation.admin import  TranslationAdmin ,TranslationTabularInline ,TranslationStackedInline
from .models import ContactUs



@admin.register(ContactUs)
class ThermalAndSoundInsulationAdmin(TranslationAdmin):
    list_display = ('address', 'phone', 'email')  # عرض هذه الحقول في واجهة الـ Admin
    search_fields = ('address', 'phone', 'email')  # يمكن البحث عن هذه الحقول


    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
        