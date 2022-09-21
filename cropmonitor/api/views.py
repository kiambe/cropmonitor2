from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from planting.models import *
from .serializers import PlantingSerializer



from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from .models import *
import ee
import pandas as pd
import altair as alt
import numpy as np
import json

 # 2. Create
    
# Trigger the authentication flow.
#ee.Authenticate()

# Initialize the library.
ee.Initialize()

geoJSON = {
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              35.473892211914062,
              0.98081240937428
            ],
            [
              35.658599853515625,
              0.98081240937428
            ],
            [
              35.658599853515625,
              0.06066538593667
            ],
            [
              35.473892211914062,
              0.06066538593667
            ],
            [
              35.473892211914062,
              0.98081240937428
            ]
          ]
        ]
      }
    }
  ]
}

coords = geoJSON['features'][0]['geometry']['coordinates']
aoi = ee.Geometry.Polygon(coords)

aoi_sub = ee.Geometry.Polygon(coords)


def create_reduce_region_function(geometry,
                                  reducer=ee.Reducer.mean(),
                                  scale=1000,
                                  crs='EPSG:4326',
                                  bestEffort=True,
                                  maxPixels=1e13,
                                  tileScale=4):
  """Creates a region reduction function.

  Creates a region reduction function intended to be used as the input function
  to ee.ImageCollection.map() for reducing pixels intersecting a provided region
  to a statistic for each image in a collection. See ee.Image.reduceRegion()
  documentation for more details.

  Args:
    geometry:
      An ee.Geometry that defines the region over which to reduce data.
    reducer:
      Optional; An ee.Reducer that defines the reduction method.
    scale:
      Optional; A number that defines the nominal scale in meters of the
      projection to work in.
    crs:
      Optional; An ee.Projection or EPSG string ('EPSG:5070') that defines
      the projection to work in.
    bestEffort:
      Optional; A Boolean indicator for whether to use a larger scale if the
      geometry contains too many pixels at the given scale for the operation
      to succeed.
    maxPixels:
      Optional; A number specifying the maximum number of pixels to reduce.
    tileScale:
      Optional; A number representing the scaling factor used to reduce
      aggregation tile size; using a larger tileScale (e.g. 2 or 4) may enable
      computations that run out of memory with the default.

  Returns:
    A function that accepts an ee.Image and reduces it by region, according to
    the provided arguments.
  """

  def reduce_region_function(img):
    """Applies the ee.Image.reduceRegion() method.

    Args:
      img:
        An ee.Image to reduce to a statistic by region.

    Returns:
      An ee.Feature that contains properties representing the image region
      reduction results per band and the image timestamp formatted as
      milliseconds from Unix epoch (included to enable time series plotting).
    """

    stat = img.reduceRegion(
        reducer=reducer,
        geometry=geometry,
        scale=scale,
        crs=crs,
        bestEffort=bestEffort,
        maxPixels=maxPixels,
        tileScale=tileScale)

    return ee.Feature(geometry, stat).set({'millis': img.date().millis()})
  return reduce_region_function




  # Define a function to transfer feature properties to a dictionary.
def fc_to_dict(fc):
  prop_names = fc.first().propertyNames()
  prop_lists = fc.reduceColumns(
      reducer=ee.Reducer.toList().repeat(prop_names.size()),
      selectors=prop_names).get('list')

  return ee.Dictionary.fromLists(prop_names, prop_lists)



today = ee.Date(pd.to_datetime('today'))
date_range = ee.DateRange(today.advance(-1, 'years'), today)




# Function to add date variables to DataFrame.
def add_date_info(df):
  df['Timestamp'] = pd.to_datetime(df['millis'], unit='ms')
  df['Year'] = pd.DatetimeIndex(df['Timestamp']).year
  df['Month'] = pd.DatetimeIndex(df['Timestamp']).month
  df['Day'] = pd.DatetimeIndex(df['Timestamp']).day
  df['DOY'] = pd.DatetimeIndex(df['Timestamp']).dayofyear
  return df

ndvi = ee.ImageCollection('MODIS/006/MOD13A2').filterDate(date_range).select('NDVI')

reduce_ndvi = create_reduce_region_function(
    geometry=aoi, reducer=ee.Reducer.mean(), scale=1000, crs='EPSG:3310')

ndvi_stat_fc = ee.FeatureCollection(ndvi.map(reduce_ndvi)).filter(
    ee.Filter.notNull(ndvi.first().bandNames()))















class PlantingPlannerListApiView(APIView):
    # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        todos = PlantingDatePlannerC.objects.all()
        serializer = PlantingSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

   



@login_required(login_url='login')
def ndvi(request):
    
   template = loader.get_template('farm/ndvi.html')
   context={

   }

   return HttpResponse(template.render(context, request))


def ndvidata(request):
    labels = []
    data = []

    ndvi_dict = fc_to_dict(ndvi_stat_fc).getInfo()
    ndvi_df = pd.DataFrame(ndvi_dict)
#display(ndvi_df)
#print(ndvi_df.dtypes)


    ndvi_df['NDVI'] = ndvi_df['NDVI'] / 10000
    ndvi_df = add_date_info(ndvi_df)

    ndvi_df = ndvi_df.reset_index()  # make sure indexes pair

    for index, row in ndvi_df.iterrows():
        labels.append(row['Timestamp'])
        data.append(row['NDVI'])


    context={
        'labels': labels,
        'data': data
    }
    return JsonResponse(data={
        'labels': labels,
        'data': data
    })