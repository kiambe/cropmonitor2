from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def login(request):
  template = loader.get_template('accounts/login.html')
  context = {
        
  }
  return HttpResponse(template.render(context, request))


def register(request):
  template = loader.get_template('accounts/register.html')
  context = {
    
    
  }
  return HttpResponse(template.render(context, request))


def home(request):
  template = loader.get_template('dashboard/home.html')
  context = {
    
    
  }
  return HttpResponse(template.render(context, request))



def contactus(request):
  template = loader.get_template('dashboard/contactus.html')
  context = {
    
    
  }
  return HttpResponse(template.render(context, request))


def faq(request):
  template = loader.get_template('dashboard/faq.html')
  context = {
    
    
  }
  return HttpResponse(template.render(context, request))




