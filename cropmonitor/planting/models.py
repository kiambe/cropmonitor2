from django.db import models

# Create your models here.


length = 2000

class ValueChain(models.Model):    
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=256, null=False)   
  def __str__(self):
        return str(self.name)


class ValueChainVariety(models.Model):    
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=256, null=False) 
  release_name = models.CharField(max_length=256, null=False)
  valuechain = models.ForeignKey(
    ValueChain, 
    on_delete=models.CASCADE,
    null=True,
    blank=True
    )

  def __str__(self):
        return str(self.release_name)
            
        
class County(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=length, blank=True, null=True,)
    lat = models.CharField(max_length=length, blank=True, null=True,)
    lng = models.CharField(max_length=length, blank=True, null=True,)
    category = models.CharField(max_length=length, blank=True, null=True,)
    code = models.CharField(max_length=length, blank=True, null=True,)
    loccode = models.CharField(max_length=length, blank=True, null=True,)
    def __str__(self):
        return '%s' % self.name


class SubCounty(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    county_id = models.ForeignKey(County, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=length, blank=True, null=True,)
    lat = models.CharField(max_length=length, blank=True, null=True,)
    lng = models.CharField(max_length=length, blank=True, null=True,)
    category = models.CharField(max_length=length, blank=True, null=True,)
    code = models.CharField(max_length=length, blank=True, null=True,)
    loccode = models.CharField(max_length=length, blank=True, null=True,)

    def __str__(self):
        return '%s' % self.name


class Ward(models.Model):
    county_id = models.ForeignKey(County, on_delete=models.CASCADE, blank=True, null=True)
    subcounty_id = models.ForeignKey(SubCounty, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=length, blank=True, null=True,)
    lat = models.CharField(max_length=length, blank=True, null=True,)
    lng = models.CharField(max_length=length, blank=True, null=True,)
    category = models.CharField(max_length=length, blank=True, null=True,)
    code = models.CharField(max_length=length, blank=True, null=True,)
    loccode = models.CharField(max_length=length, blank=True, null=True,)

    def __str__(self):
        return '%s' % self.name     




class CropCalendar(models.Model):
  id = models.AutoField(primary_key=True)

  county = models.ForeignKey(
    County, 
    on_delete=models.CASCADE,
    null=False
    )


  subcounty = models.ForeignKey(
    SubCounty, 
    on_delete=models.CASCADE,
    null=True,
    blank=True
    )


  ward = models.ForeignKey(
    Ward, 
    on_delete=models.CASCADE,
    null=True,
    blank=True
    )

  valuechain = models.ForeignKey(
    ValueChain, 
    on_delete=models.CASCADE, 
    null=False
    ) 


  refyear = models.IntegerField(default=2022, null=True, blank=True)  
 
  sow_start_date = models.DateField(
    null=True,
    blank=True
    ) 

  sow_end_date = models.DateField(
    null=True,
    blank=True
    )
  season = models.IntegerField(default=1, null=True, blank=True)  
  date_created = models.DateTimeField(auto_now_add=True)
  date_updated = models.DateTimeField(auto_now=True)
  def __str__(self):
        return str(self.valuechain)
  



class PlantingDatePlannerC(models.Model):
  id = models.AutoField(primary_key=True) 
  county = models.ForeignKey(
    County, 
    on_delete=models.CASCADE,
    null=False
    )


  subcounty = models.ForeignKey(
    SubCounty, 
    on_delete=models.CASCADE,
    null=True,
    blank=True
    )


  ward = models.ForeignKey(
    Ward, 
    on_delete=models.CASCADE,
    null=True,
    blank=True
    )

  valuechain = models.ForeignKey(
    ValueChain, 
    on_delete=models.CASCADE, 
    
    null=True,
    blank=True
    ) 
  vc_variety = models.ForeignKey(
    ValueChainVariety, 
    on_delete=models.CASCADE,     
    null=True,
    blank=True
    ) 
   

  refyear = models.IntegerField(default=2022, null=True, blank=True)  
  sow_start_date = models.DateField(
    null=True,
    blank=True
    ) 

  sow_end_date = models.DateField(
    null=True,
    blank=True
    )

  season = models.IntegerField(default=1, null=True, blank=True)     
  min_maturity_period = models.IntegerField(default=90, null=True, blank=True) 
  max_maturity_period = models.IntegerField(default=90, null=True, blank=True) 
  first_weeding_after_days = models.TextField(null=True, blank=True)
  second_weeding_after_days = models.TextField(null=True, blank=True)
  ferlizer_application_recommendation = models.TextField(null=True, blank=True)
  min_expected_yield = models.FloatField(default=1.9, null=True, blank=True)
  max_expected_yield = models.FloatField(default=1.9, null=True, blank=True)
  areas_for_optimal_production = models.CharField(max_length=256, null=True, blank=True)
  special_attributes = models.CharField(max_length=256, null=True, blank=True) 
  date_created = models.DateTimeField(auto_now_add=True)
  date_updated = models.DateTimeField(auto_now=True)
  def __str__(self):
        return str(self.valuechain)