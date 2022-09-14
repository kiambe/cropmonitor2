"""cropmonitor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.train_cassava, name="train_home"),
    path('train_cassava/', views.train_cassava, name="train_cassava"),
    path('train_fingermillet/', views.train_fingermillet, name="train_fingermillet"),
    path('train_greengrams/', views.train_greengrams, name="train_greengrams"),
    path('train_pigeonpeas/', views.train_pigeonpeas, name="train_pigeonpeas"),
    path('train_sorghum/', views.train_sorghum, name="train_sorghum"),
]