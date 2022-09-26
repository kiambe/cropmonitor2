from codecs import getencoder
from django.db import models
from planting.models import *
from accounts.models import FarmerProfile
from django.contrib.auth.models import User

# Create your models here.



class FarmOwnership(models.Model):    
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=256, null=False) 
  def __str__(self):
        return str(self.name)

class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    telephone = models.IntegerField(null=True, blank=True)
    mobile  = models.IntegerField(null=True, blank=True)
    year_of_birth= models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    county = models.CharField(max_length=20, null=True, blank=True)
    subcounty = models.CharField(max_length=20, null=True, blank=True)
    ward = models.CharField(max_length=20, null=True, blank=True)
    lat = models.FloatField(max_length=20, null=True, blank=True)
    lon = models.FloatField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
     

    def __str__(self):
        return f'{self.user.username} Profile' #show how we want it to be displayed

STATUS = (
    (0,"Idle Land"),
    (1,"Active Land")
)

class MyFarm(models.Model):
  id = models.AutoField(primary_key=True) 
  farm_name = models.CharField(max_length=256, null=True, blank=True) 
  slug = models.SlugField(max_length=250, null = True, blank = True)
  valuechain = models.ForeignKey(
    ValueChain, 
    on_delete=models.CASCADE, 
    null=True, blank=True
    )     
  vc_variety = models.ForeignKey(
    ValueChainVariety, 
    on_delete=models.CASCADE, 
    null=True, blank=True
    )  
  owner = models.ForeignKey(
    User, 
    on_delete=models.CASCADE, related_name='my_farms'
    )
  farm_ownership = models.ForeignKey(
    FarmOwnership, 
    on_delete=models.CASCADE, 
    null=False
    ) 
  county = models.ForeignKey(
    County, 
    on_delete=models.CASCADE,
    null=False
    )
  subcounty = models.ForeignKey(
    SubCounty, 
    on_delete=models.CASCADE,
    null=False
    )
  ward = models.ForeignKey(
    Ward, 
    on_delete=models.CASCADE,
    null=False
    )
  lat = models.FloatField(max_length=20, null=True, blank=True)
  lon = models.FloatField(max_length=20, null=True, blank=True)
  farm_size_ha = models.FloatField(max_length=20, null=True, blank=True)
  date_created = models.DateTimeField(auto_now_add=True)
  date_updated = models.DateTimeField(auto_now=True)
  status = models.IntegerField(choices=STATUS, default=0)

  class Meta:
        ordering = ['-date_created']

  def __str__(self):
        return self.farm_name

