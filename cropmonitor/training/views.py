from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def train_fingermillet(request):
  template = loader.get_template('training/train_fingermillet.html')
  context = {
    
    
  }
  return HttpResponse(template.render(context, request))


def train_sorghum(request):
  template = loader.get_template('training/train_sorghum.html')
  context = {
    
    
  }
  return HttpResponse(template.render(context, request))


def train_cassava(request):
  template = loader.get_template('training/train_cassava.html')
  context = {
    
    
  }
  return HttpResponse(template.render(context, request))


def train_greengrams(request):
  template = loader.get_template('training/train_greengrams.html')
  context = {
    
    
  }
  return HttpResponse(template.render(context, request))

def train_pigeonpeas(request):
  template = loader.get_template('training/train_pigeonpeas.html')
  context = {
    
    
  }
  return HttpResponse(template.render(context, request))