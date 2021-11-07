from django.http import HttpResponse
from django.shortcuts import render
import numpy as np
from . import dopelganger_OOP as dop
import random


def about(request):
    return HttpResponse('About page')


def home(request):
    mileage_per_day = np.mean(dop.Generator(365, 50, 2).array_generation())
    mileage_per_year = np.sum(mileage_per_day)
    number_of_tech_actions = mileage_per_year/15000
    fuel_consumption = mileage_per_year*10/100
    number_of_failures = mileage_per_year * random.uniform(1/20000, 1/mileage_per_year)
    dict_array = {'mileage_per_day': "%.2f" % mileage_per_day,
                  'mileage_per_year': "%.2f" % mileage_per_year,
                  'number_of_tech_actions': "%.2f" % number_of_tech_actions,
                  'fuel_consumption': "%.2f" % fuel_consumption,
                  'number_of_failures': "%.2f" % number_of_failures,
                  }
    return render(request, 'home.html', dict_array)



