from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .models import *
# Create your views here.

import datetime
import time
from datetime import timedelta


def planner(request):
    
    template = loader.get_template('planting/planner.html')
    planners = PlantingDatePlanner.objects.all()
    cnow = datetime.datetime.now()

    #from datetime import date
    
    #print datetime.now() + timedelta(days=1)
    cnow = cnow + timedelta(days=90)
    
    context = {
        'planners':planners,
        #'myFilter': myFilter,
        'cnow': cnow,
        
    }
    return HttpResponse(template.render(context, request))

