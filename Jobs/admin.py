from django.contrib import admin
from .models import *
from modeltranslation.admin import  TranslationAdmin ,TranslationTabularInline ,TranslationStackedInline




@admin.register(JobInfo)
class RoadsideAssistanceSliderAdmin(TranslationAdmin):
    list_display = ('image_tag','title',)
    list_display_links = ('image_tag','title',) 


    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
        




class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'job_title', 'experience_years', 'created_at')
    readonly_fields = ('name', 'email', 'phone_number', 'job_title', 'experience_years', 'resume', 'portfolio', 'about','created_at')

admin.site.register(JobApplication, JobApplicationAdmin)
