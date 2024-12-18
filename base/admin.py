from django.contrib import admin
from modeltranslation.admin import  TranslationAdmin ,TranslationTabularInline ,TranslationStackedInline
from .models import ContactUs



@admin.register(ContactUs)
class ThermalAndSoundInsulationAdmin(admin.ModelAdmin):
    list_display = ('address', 'phone', 'email')  # عرض هذه الحقول في واجهة الـ Admin
    search_fields = ('address', 'phone', 'email')  # يمكن البحث عن هذه الحقول

