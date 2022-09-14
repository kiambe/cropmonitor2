from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def kaop(request):
  template = loader.get_template('rlinks/kaop.html')
  context = {
    
    
  }
  return HttpResponse(template.render(context, request))


def kamis(request):
  template = loader.get_template('rlinks/kamis.html')
  context = {
    
    
  }
  return HttpResponse(template.render(context, request))


def selector(request):
  template = loader.get_template('rlinks/selector.html')
  context = {
    
    
  }
  return HttpResponse(template.render(context, request))


