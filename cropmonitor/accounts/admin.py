from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(FarmerProfile)
class MyFarmAdmin(admin.ModelAdmin):
  list_display = ('id','firstname' , 'tel', 'gender', 'county', 'national_id')

