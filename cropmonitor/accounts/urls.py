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
    path('', views.login, name="login"),
   
    path('register', views.register, name="register"),
    path('home', views.home, name="home"),    
    #path('myprofile', views.myprofile, name="myprofile"),  
    path('contactus', views.contactus, name="contactus"),
    path('faq', views.faq, name="faq"),
    path('logout', views.logout, name="logout"),
    path('myprofile/', views.ProfileView.as_view(), name='myprofile'),

    
    #path('api/', include(router.urls)),
    #path('api-token-auth/', views.obtain_auth_token, name='api-tokn-auth'),





]