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

from .filters import PlannerFilter


from django_filters.views import FilterView
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def planner(request):
    
    template = loader.get_template('planting/planner.html')
    planners = PlantingDatePlannerC.objects.all()
    counties = County.objects.all()
    subcounties = SubCounty.objects.all()
    wards = Ward.objects.all()
    vc = ValueChain.objects.all()
    varieties= PlantingDatePlannerC.objects.all()

    #counties = PlantingDatePlannerC.objects.all().values('county').distinct()
    #cnow = datetime.datetime.now()

    #from datetime import date
    
    #print datetime.now() + timedelta(days=1)
   # cnow = cnow + timedelta(days=90)

    myFilter = PlannerFilter(request.GET, queryset=planners)
                                                                
   
    
    
    context = {
        'planners':planners,
        'counties':counties,
        'varieties': varieties,
        'vc': vc,
        'subcounties': subcounties,
        'wards': wards,
        'varieties': varieties,

        'myFilter': myFilter,
        #'cnow': cnow,
        
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='login')
def plantingadvisories(request):
    
    template = loader.get_template('planting/plantingadvisories.html')
    planners = PlantingDatePlannerC.objects.all()

    myFilter = PlannerFilter(request.GET, queryset=planners)
                                                                
   
    
    
    context = {
        'planners':planners,

        'myFilter': myFilter,
        
    }
    return HttpResponse(template.render(context, request))

