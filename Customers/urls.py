from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('verify-otp/', verify_otp_view, name='verify_otp'),
    
    
    path('profile/', profile_view, name='profile'),  
    path('update-profile/',update_profile_view, name='update_profile'),
]
