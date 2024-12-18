from django.contrib import admin
from django.utils.safestring import mark_safe  # استيراد mark_safe
from .models import Location

class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'google_map_link')  # عرض اسم الموقع ورابط جوجل ماب في القائمة

    # دالة لعرض رابط جوجل ماب
    def google_map_link(self, obj):
        return mark_safe(f'<a href="https://www.google.com/maps?q={obj.latitude},{obj.longitude}" target="_blank">الموقع </a>')

    # جعل اسم الموقع قابل للنقر للوصول إلى جوجل ماب
    def name(self, obj):
        return mark_safe(f'<a href="https://www.google.com/maps?q={obj.latitude},{obj.longitude}" target="_blank">{obj.name}</a>')

admin.site.register(Location, LocationAdmin)
