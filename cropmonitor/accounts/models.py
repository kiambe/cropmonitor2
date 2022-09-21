from django.db import models
from planting.models import County, SubCounty, Ward

# Create your models here.

class FarmerProfile(models.Model):    
  id = models.AutoField(primary_key=True)
  firstname = models.CharField(max_length=256, null=True, blank=True)
  lastfirstname = models.CharField(max_length=256, null=True, blank=True)
  tel = models.CharField(max_length=10, null=True, blank=True)
  
  county = models.ForeignKey(
    County, 
    on_delete=models.CASCADE,
    null=True, blank=True
    )
  subcounty = models.ForeignKey(
    SubCounty, 
    on_delete=models.CASCADE,
    null=True, blank=True
    )
  ward = models.ForeignKey(
    Ward, 
    on_delete=models.CASCADE,
    null=True, blank=True
    )  
  yob = models.IntegerField (null=True, blank=True)
  national_id = models.CharField(max_length=25, null=True, blank=True)
  gender = models.CharField(max_length=10, null=True, blank=True) 
  phone = models.CharField(max_length=15, null=True, blank=True)
  def __str__(self):
        return str(self.national_id)

    



