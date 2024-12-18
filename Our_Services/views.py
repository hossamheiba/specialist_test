from .models import *
from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext as _


# Mechanics ------------------------------------------------------
def mechanics_view(request):
    mechanics = Mechanics.objects.first()
    if not mechanics:
        return render(request, 'Mechanics.html', {
            'error_message': _('No data available to display at the moment.'),  
        })
    sliders = mechanics.sliders.all()
    return render(request, 'Mechanics.html', {
        'mechanics': mechanics,
        'sliders': sliders,
    })
    
    
# Electricity ------------------------------------------------------
def electricity_view(request):
    electricity = Electricity.objects.first()
    if not electricity:
        return render(request, 'Electricity.html', {
            'error_message': _('No data available to display at the moment.'),
        })
    sliders = electricity.sliders.all()
    return render(request, 'Electricity.html', {
        'electricity': electricity,
        'sliders': sliders,
    })
    

# BodyworkAndPainting ------------------------------------------------------
def bodyworkandpainting_view(request):
    bodyworkandpainting = BodyworkAndPainting.objects.first()
    if not bodyworkandpainting:
        return render(request, 'Bodywork_and_painting.html', {
            'error_message': _('No data available to display at the moment.'),
        })
    sliders = bodyworkandpainting.sliders.all()
    return render(request, 'Bodywork_and_painting.html', {
        'bodyworkandpainting': bodyworkandpainting,
        'sliders': sliders,
    })



# ThermalAndSoundInsulation ------------------------------------------------------
def thermalandsoundinsulation_view(request):
    thermalandsoundinsulation = ThermalAndSoundInsulation.objects.first()
    if not thermalandsoundinsulation:
        return render(request, 'Thermal_And_Soundin_Sulation.html', {
            'error_message': _('No data available to display at the moment.'),
        })
    sliders = thermalandsoundinsulation.sliders.all()
    return render(request, 'Thermal_And_Soundin_Sulation.html', {
        'thermalandsoundinsulation': thermalandsoundinsulation,
        'sliders': sliders,
    })





# CarProgramming ------------------------------------------------------
def carprogramming_view(request):
    carprogramming = CarProgramming.objects.first()
    if not carprogramming:
        return render(request, 'CarProgramming.html', {
            'error_message': _('No data available to display at the moment.'),
        })
    sliders = carprogramming.sliders.all()
    return render(request, 'CarProgramming.html', {
        'carprogramming': carprogramming,
        'sliders': sliders,
    })




# SportsSuspension ------------------------------------------------------
def sportssuspension_view(request):
    sportssuspension = SportsSuspension.objects.first()
    if not sportssuspension:
        return render(request, 'SportsSuspension.html', {
            'error_message': _('No data available to display at the moment.'),
        })
    sliders = sportssuspension.sliders.all()
    return render(request, 'SportsSuspension.html', {
        'sportssuspension': sportssuspension,
        'sliders': sliders,
    })


# RoadsideAssistance ------------------------------------------------------
def roadsideassistance_view(request):
    roadsideassistance = RoadsideAssistance.objects.first()
    if not roadsideassistance:
        return render(request, 'Roadside_Assistance.html', {
            'error_message': _('No data available to display at the moment.'),
        })
    sliders = roadsideassistance.sliders.all()
    return render(request, 'Roadside_Assistance.html', {
        'roadsideassistance': roadsideassistance,
        'sliders': sliders,
    })






