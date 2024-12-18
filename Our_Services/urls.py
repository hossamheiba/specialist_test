from django.urls import path
from . import views

app_name = "Our_Services"

urlpatterns = [
    path('mechanics/', views.mechanics_view, name='mechanics_view'),
    path('electricity/', views.electricity_view, name='electricity_view'),
    path('bodyworkandpainting/', views.bodyworkandpainting_view, name='bodyworkandpainting_view'),
    path('thermalandsoundinsulation/', views.thermalandsoundinsulation_view, name='thermalandsoundinsulation_view'),
    path('carprogramming/', views.carprogramming_view, name='carprogramming_view'),
    path('sportssuspension/', views.sportssuspension_view, name='sportssuspension_view'),
    path('roadsideassistance/', views.roadsideassistance_view, name='roadsideassistance_view'),
]
