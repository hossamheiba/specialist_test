from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe 

admin.site.register(DiscountCoupon)
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1

class CarBrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    inlines = [CarModelInline]



class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 
        'last_name', 
        'phone_number', 
        'car_brand', 
        'car_model', 
        'engine_type', 
        'manufacturing_year', 
        'created_at', 
        'appointment_date', 
        'formatted_appointment_time',  # عرض الوقت بتنسيق 12 ساعة
        'formatted_discount_value',  
    )
    readonly_fields = (
        'first_name', 
        'last_name', 
        'phone_number', 
        'car_brand', 
        'car_model', 
        'engine_type', 
        'manufacturing_year', 
        'created_at', 
        'appointment_date', 
        'formatted_appointment_time', 
        'formatted_discount_value', 
        'notes', 
    )

    search_fields = (
        'first_name', 
        'last_name', 
        'phone_number', 
        'car_brand__name',    
        'car_model__name',   
        'engine_type__name',  
        'manufacturing_year', 
        'appointment_date', 
        'appointment_time'
    )

    list_filter = (
        'first_name', 
        'last_name', 
        'phone_number', 
        'car_brand', 
        'car_model', 
        'engine_type', 
        'manufacturing_year', 
        'appointment_date', 
        'appointment_time'
    )

    def formatted_appointment_time(self, obj):
        return obj.appointment_time.strftime("%I %p") if obj.appointment_time else None

    formatted_appointment_time.short_description = 'Appointment Time'

    def formatted_discount_value(self, obj):
        return f"{obj.discount_value}%" if obj.discount_value is not None else None

    formatted_discount_value.short_description = 'Discount Value'


class UnavailableDateAdmin(admin.ModelAdmin):
    list_display = ('date',)

class LocationAdmin(admin.ModelAdmin):
    readonly_fields = ('first_name' , 'last_name' ,'phone_number' , 'Date_of_submission')

    list_display = ('first_name' , 'last_name' ,'phone_number','Date_of_submission' ,'google_map_link')
    exclude = ('latitude', 'longitude')
    
    
    def google_map_link(self, obj):
        if obj.latitude and obj.longitude:
            return mark_safe(f'<a href="https://www.google.com/maps?q={obj.latitude},{obj.longitude}" target="_blank">View Location on Google Maps</a>')
        return "No Coordinates"  # إذا كانت الإحداثيات غير موجودة

    google_map_link.short_description = 'Google Map Link'  # تغيير العنوان في الـ Admin

admin.site.register(CarBrand, CarBrandAdmin)
admin.site.register(EngineType)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(UnavailableDate, UnavailableDateAdmin)
admin.site.register(Location, LocationAdmin)




    
    # # دالة لعرض رابط جوجل ماب
    # def google_map_link(self, obj):
    #     return mark_safe(f'<a href="https://www.google.com/maps?q={obj.latitude},{obj.longitude}" target="_blank">Location </a>')

    # # جعل اسم الموقع قابل للنقر للوصول إلى جوجل ماب
    # def name(self, obj):
    #     return mark_safe(f'<a href="https://www.google.com/maps?q={obj.latitude},{obj.longitude}" target="_blank"></a>')