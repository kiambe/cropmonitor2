from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def myfarms(request):
  template = loader.get_template('farm/myfarms.html')
  context = {
    
    
  }
  return HttpResponse(template.render(context, request))


def farmsummary(request):
  template = loader.get_template('farm/farmsummary.html')
  context = {
    
    
  }
  return HttpResponse(template.render(context, request))
