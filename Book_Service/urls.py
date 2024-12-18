from django.urls import path
from . import views


app_name = "Book_Service"

urlpatterns = [
    path('', views.location_appointment, name='book_service'),
    path('book_appointment/', views.book_appointment, name='book_appointment'),
    path('send_location/', views.submit_location, name='submit_location'),
    
    path('done_appointment/', views.success_done_appointment, name='done_appointment'),
    path('done_location/', views.success_done_location, name='done_location'),
    
    
    path("appointments/", views.appointments_view, name="appointments_view"),
    path("get_car_models/", views.get_car_models, name="get_car_models"),
    path('check_coupon/', views.check_coupon, name='check_coupon'),


    
]
