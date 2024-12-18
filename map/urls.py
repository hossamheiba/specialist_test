from django.urls import path
from . import views

urlpatterns = [
    path('', views.select_location, name='select_location'),
]
