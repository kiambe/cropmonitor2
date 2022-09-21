from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(MyFarm)
class MyFarmAdmin(admin.ModelAdmin):
  list_display = ('id', 'owner', 'farm_name' , 'valuechain',  'county')

admin.site.register(Profile)


@admin.register(FarmOwnership)
class FarmOwnershipAdmin(admin.ModelAdmin):
  list_display = ('id','name')
