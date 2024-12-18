from django.db import models
from Customers.models import UserProfile
from datetime import date
from django.utils import timezone  # تأكد من أن هذا السطر موجود في أعلى الملف

class CarBrand(models.Model):
    name = models.CharField(max_length=100, verbose_name="Car Brand")

    def __str__(self):
        return self.name

class CarModel(models.Model):
    name = models.CharField(max_length=100, verbose_name="Car Model")
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, related_name="models", verbose_name="Brand")

    def __str__(self):
        return self.name

class EngineType(models.Model):
    name = models.CharField(max_length=50, verbose_name="Engine Type")

    def __str__(self):
        return self.name

class DiscountCoupon(models.Model):
    code = models.CharField(max_length=50, unique=True, verbose_name="Coupon Code")
    discount_value = models.IntegerField(verbose_name="Discount Value")
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creation Date")
    expiration_date = models.DateTimeField(null=True, blank=True)  


    def __str__(self):
        return f"Coupon {self.code}"

    def deactivate_if_expired(self):
        if self.expiration_date and self.expiration_date < timezone.now():
            self.is_active = False
            self.save()

    def is_valid(self):
        self.deactivate_if_expired()  
        return self.is_active and self.expiration_date >= date.today()

# نموذج Appointment
class Appointment(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    last_name = models.CharField(max_length=100, verbose_name="Last Name")
    phone_number = models.CharField(max_length=15, verbose_name="Phone Number")
    car_brand = models.ForeignKey(CarBrand, on_delete=models.SET_NULL, null=True, verbose_name="Car Brand")
    car_model = models.ForeignKey(CarModel, on_delete=models.SET_NULL, null=True, verbose_name="Car Model")
    engine_type = models.ForeignKey(EngineType, on_delete=models.SET_NULL, null=True, verbose_name="Engine Type")
    manufacturing_year = models.IntegerField(verbose_name="Manufacturing Year")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creation Date")

    appointment_date = models.DateField(verbose_name="Appointment Date")
    appointment_time = models.TimeField(verbose_name="Appointment Time")
    notes = models.TextField(blank=True, null=True, verbose_name="Notes")
    coupon = models.ForeignKey(DiscountCoupon, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Coupon")
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    
    def __str__(self):
        return f"{self.appointment_date} at {self.appointment_time}"
    
    
    def apply_coupon(self):
        if self.coupon and self.coupon.is_valid():
            return self.coupon.discount_value
        return 0 




# نموذج Location
class Location(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    last_name = models.CharField(max_length=100, verbose_name="Last Name")
    phone_number = models.CharField(max_length=15, verbose_name="Phone Number")
    Date_of_submission = models.DateTimeField(null=True, blank=True, verbose_name="Date_of_submission")

    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)


    @property
    def google_map_link(self):
        return f"https://www.google.com/maps?q={self.latitude},{self.longitude}"





class UnavailableDate(models.Model):
    date = models.DateField(verbose_name="Unavailable Date")

    def __str__(self):
        return f"Unavailable: {self.date}"