from operator import concat
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader



from django.template.context import RequestContext
import pandas as pd


from .models import *

import json
import requests
import pandas as pd

import numpy
import matplotlib.pyplot as plt

from django.contrib.auth.decorators import login_required
from slugify import slugify

from django.views import View
from .forms import RegisterFarmForm, form_validation_error
from django.contrib import messages

#Mapping
import folium
from geopy.geocoders import Nominatim




@login_required(login_url='login')
def myfarms(request):
  farms=MyFarm.objects.filter(owner=request.user)
  template = loader.get_template('farm/myfarms.html')

    # calling the Nominatim tool
  loc = Nominatim(user_agent="GetLoc")
 
# entering the location name
  getLoc = loc.geocode("Gosainganj Lucknow")
 
# printing address
  #print(getLoc.address)
 
# printing latitude and longitude
  #print("Latitude = ", getLoc.latitude, "\n")
  #print("Longitude = ", getLoc.longitude)
  clat = getLoc.latitude
  clon=getLoc.longitude
  form = RegisterFarmForm(request.POST or None)
  if request.method=='POST':
    #farm_name=request.POST['farm_name'] 
    farm_name=request.POST.get('farm_name')
    slugname =slugify(farm_name) 

    
    vc_variety=request.POST.get('vc_variety')
    valuechain=request.POST.get('valuechain')
    farm_ownership=request.POST.get('farm_ownership')
    county=request.POST.get('county')
    subcounty=request.POST.get('subcounty')
    ward=request.POST.get('ward')
    lat=request.POST.get('lat')
    lon=request.POST.get('lon')
    farm_size_ha=request.POST.get('farm_size_ha')
    #newfarm.save()
    valuechain=ValueChain.objects.get(id = valuechain)
    vc_variety=ValueChainVariety.objects.get(id = vc_variety)
    farm_ownership=FarmOwnership.objects.get(id = farm_ownership)
    county=County.objects.get(id = county)
    subcounty=SubCounty.objects.get(id = subcounty)
    ward=Ward.objects.get(id = ward)





    farm=MyFarm.objects.create(farm_name=farm_name,
                              owner=request.user, 
                              farm_size_ha=farm_size_ha, 
                              lat=lat, 
                              lon=lon, 
                              valuechain=valuechain, 
                              farm_ownership=farm_ownership,
                              county=county,
                              vc_variety=vc_variety,
                              subcounty=subcounty,
                              ward=ward,
                              slug=slugname
                              
                              
                              )
    
    farm.save()
    messages.success(request,'Data has been submitted')
    

  # add the dictionary during initialization
  
  
  context = {
    "farms": farms, "clat": clat, "clon":clon, "form":form
    
    
  }
  return HttpResponse(template.render(context, request))

@login_required(login_url='login')
def farmsummary(request, slug):
  selectedfarm=MyFarm.objects.filter(slug=slug).filter(owner=request.user).first()
  latm='lat'
  lonm='lon'
  lat = getattr(selectedfarm, latm)
  lon = getattr(selectedfarm, lonm)
  
  lonlat = " {} , {}".format(lon, lat)



  

  template = loader.get_template('farm/farmsummary.html')
  
 # lat=0.4233
 # lon=35.2133

  # temperatureMin,temperatureMax,windSpeed,humidity,rainAccumulation,precipitationProbability,cloudCover,weatherCode&timesteps=1d&units=metric&apikey=$api_key



  url = "https://api.tomorrow.io/v4/timelines"
    
  querystring = {
        "location":lonlat,
        "fields":["humidity", "cloudCover", "temperature", "temperatureMin", "temperatureMax", "windSpeed", "rainAccumulation", "precipitationProbability"],
        "units":"metric",
        "timesteps":"1d",
        "startTime": "now",
        "apikey":"F1TapOsHr0SAqWmts8G1cNHJcqv4aL6I"
        }

  response = requests.request("GET", url, params=querystring)
  results = response.json()['data']['timelines'][0]['intervals']
    
  humidity = []
  temperature = [] 
  cloudCover = []
  temperatureMin = []
  temperatureMax = []
  windSpeed = []
  rainAccumulation = []
  precipitationProbability = []
    
  start_times=[]
  for x in results:
        start_times.append(x["startTime"])
        humidity.append(x["values"]["humidity"])
        cloudCover.append(x["values"]["cloudCover"])
        temperature.append(x["values"]["temperature"])
        temperatureMin.append(x["values"]["temperatureMin"])
        temperatureMax.append(x["values"]["temperatureMax"])
        windSpeed.append(x["values"]["windSpeed"])
        rainAccumulation.append(x["values"]["rainAccumulation"])
        precipitationProbability.append(x["values"]["precipitationProbability"])
                
              
  pdata = pd.DataFrame(
                {
                    "Start_time": start_times,
                    "humidity": humidity,
                    "cloudCover":cloudCover,
                    "temperature":temperature,
                    "temperatureMin":temperatureMin,
                    "temperatureMax": temperatureMax,
                    "windSpeed": windSpeed,
                    "rainAccumulation": rainAccumulation,
                    "precipitationProbability": precipitationProbability
                },
            )

  pdata_json =pdata.to_json()


  
    # parsing the DataFrame in json format.
  json_records = pdata.reset_index().to_json(orient ='records')
  wdata = []
  wdata = json.loads(json_records)
  context = {'wdata': wdata}


  #Mapping
  farmloc=[lat,lon]
  map= folium.Map(location=[lat,lon], zoom_start=15)

  folium.Marker(farmloc).add_to(map)
  #folium.raster_layers.TileLayer('Stamen Terrain').add_to(map)
  #folium.raster_layers.TileLayer('Stamen Toner').add_to(map)
  #folium.raster_layers.TileLayer('Stamen Watercolor').add_to(map)
  folium.LayerControl().add_to(map)
  map = map._repr_html_()
    
  context = {
      
      "pdata_json":pdata_json,
      "pdata":pdata,
      "wdata":wdata,
      "selectedfarm":selectedfarm,
      'lat':lat,
      'map':map,

     

    }
    
  return HttpResponse(template.render(context, request))




@login_required(login_url='login')
def registerfarm(request):
  # calling the Nominatim tool
  loc = Nominatim(user_agent="GetLoc")
 
# entering the location name
  getLoc = loc.geocode("Gosainganj Lucknow")
 
# printing address
  #print(getLoc.address)
 
# printing latitude and longitude
  #print("Latitude = ", getLoc.latitude, "\n")
  #print("Longitude = ", getLoc.longitude)
  clat = getLoc.latitude
  clon=getLoc.longitude
  form = RegisterFarmForm(request.POST or None)
  if request.method=='POST':
    #farm_name=request.POST['farm_name'] 
    farm_name=request.POST.get('farm_name')
    #farm_name =slugify(farm_name) 

   # newfarm=MyFarm()
   ## newfarm.owner= request.user
   # newfarm.farm_name=request.POST.get('farm_name')
   # newfarm.slug=farm_name
    
    vc_variety=request.POST.get('vc_variety')
    farm_ownership=request.POST.get('farm_ownership')
    county=request.POST.get('county')
    subcounty=request.POST.get('subcounty')
    ward=request.POST.get('ward')
    lat=request.POST.get('lat')
    lon=request.POST.get('lon')
    farm_size_ha=request.POST.get('farm_size_ha')
    #newfarm.save()
    farm=MyFarm.objects.create(farm_name=farm_name,owner=request.user)
    farm.save
    messages.success(request,'Data has been submitted')
    

  farms=MyFarm.objects.filter(owner=request.user)
  template = loader.get_template('farm/myfarms.html')
  context = {
    "farms": farms,"form": form, "clat":clat, "clon":clon,
    
    
  }
  #return HttpResponse(template.render(context, request))
  return redirect('myfarms')

'''
@login_required(login_url='login')
class FarmView(View):
    farm = None

    def dispatch(self, request, *args, **kwargs):
        self.profile, __ = MyFarm.objects.get_or_create(user=request.user)
        return super(FarmView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        context = {'farm': self.farm, 'segment': 'farm'}
        return render(request, 'farm/myfarms.html', context)

    def post(self, request):
        form = RegisterFarmForm(request.POST, request.FILES, instance=self.profile)

        if form.is_valid():
            farm = form.save()
            #farm.user.first_name = form.cleaned_data.get('first_name')
            #farm.user.last_name = form.cleaned_data.get('last_name')
            #farm.user.email = form.cleaned_data.get('email')
            farm.user.save()

            messages.success(request, 'Farm registered successfully')
        else:
            messages.error(request, form_validation_error(form))
        return redirect('myfarms')


def contact(request):
    if request.method=='POST':
        full_name=request.POST['full_name']
        email=request.POST['email']
        message=request.POST['message']
        contact=Contact.objects.create(full_name=full_name,email=email,message=message)
        messages.success(request,'Data has been submitted')
    return render(request,'contact.html')
    '''


@login_required(login_url='login')
def registerfarm2(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
    farmform = RegisterFarmForm(request.POST or None)
    if request.method=='POST':
 
    # add the dictionary during initialization
      farmform = RegisterFarmForm(request.POST or None)
      if farmform.is_valid():
        farm=farmform.save(commit=False)
         
    #context['form']= form
        farm = farmform.save(commit=False)
        farm.owner = request.user
        farm.save()
    
    farms=MyFarm.objects.filter(owner=request.user)
    context ={'farmform':farmform, 'farms': farms}
    #context ={'farmform':farmform}
    template = loader.get_template('farm/myfarms.html')
    return HttpResponse(template.render(context, request))
    #return render(request, 'farm/myfarms.html', context)



@login_required(login_url='login')
def emp(request):  
    if request.method == "POST":  
        form = RegisterFarmForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('farm/myfarms.html')  
            except:  
                pass  
    else:  
        form = RegisterFarmForm()  
    return render(request,'farm/myfarms.html',{'form':form})  



class RegisterFarmView(View):
    farm = None

    

    def get(self, request):
        #context = {'farm': self.farm, 'segment': 'farm'}
        farms=MyFarm.objects.filter(owner=request.user)
        farmform = RegisterFarmForm(request.POST, request.FILES, instance=self.farm)
        context ={'farmform':farmform, 'farms': farms}
        return render(request, 'farm/myfarms.html', context)

    def post(self, request):
        form = RegisterFarmForm(request.POST, request.FILES, instance=self.farm)

        if form.is_valid():
            farm = form.save()
            farm.owner = request.user
            farm.save()
            #profile.user.first_name = form.cleaned_data.get('first_name')
            #profile.user.last_name = form.cleaned_data.get('last_name')
            #profile.user.email = form.cleaned_data.get('email')
            #profile.user.save()

            messages.success(request, 'Profile saved successfully')
        else:
            messages.error(request, form_validation_error(form))
        return redirect('farm/myfarms.html')

