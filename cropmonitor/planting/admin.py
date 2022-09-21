from multiprocessing import Value
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.

from .models import *

class CountyAdmin(ImportExportModelAdmin):
    list_display = ("id", "name", "lat", "lng", "category", "code", "loccode")
    pass
admin.site.register(County, CountyAdmin)


@admin.register(SubCounty)
class SubCountyAdmin(ImportExportModelAdmin):
    list_display = ("id", "county_id", "name", "lat",
                    "lng", "category", "code", "loccode")
    pass

@admin.register(Ward)
class WardAdmin(ImportExportModelAdmin):
    list_display = ("id", "county_id", "subcounty_id", "name",
                    "lat", "lng", "category", "code", "loccode")
    pass


admin.site.register(ValueChain)
admin.site.register(ValueChainVariety) 
admin.site.register(CropCalendar) 



@admin.register(PlantingDatePlannerC)
class plantingDateCAdmin(admin.ModelAdmin):
  list_display = ('id','county' , 'vc_variety',  'min_maturity_period')

