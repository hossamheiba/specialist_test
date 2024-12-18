from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)  # اسم الموقع
    latitude = models.FloatField()  # خط العرض
    longitude = models.FloatField()  # خط الطول

    def __str__(self):
        return self.name

    @property
    def google_map_link(self):
        # إنشاء الرابط الخاص بجوجل ماب بناءً على الإحداثيات
        return f"https://www.google.com/maps?q={self.latitude},{self.longitude}"




