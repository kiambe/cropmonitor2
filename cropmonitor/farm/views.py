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



@login_required(login_url='login')
def myfarms(request):
  template = loader.get_template('farm/myfarms.html')
  context = {
    
    
  }
  return HttpResponse(template.render(context, request))

@login_required(login_url='login')
def farmsummary(request):
  template = loader.get_template('farm/farmsummary.html')
  
  lat=0.4233
  lon=35.2133

  # temperatureMin,temperatureMax,windSpeed,humidity,rainAccumulation,precipitationProbability,cloudCover,weatherCode&timesteps=1d&units=metric&apikey=$api_key



  url = "https://api.tomorrow.io/v4/timelines"
    
  querystring = {
        "location":"35.2133, 0.4233",
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
    
  context = {
      
      "pdata_json":pdata_json,
      "pdata":pdata,
      "wdata":wdata,

     

    }
    
  return HttpResponse(template.render(context, request))




