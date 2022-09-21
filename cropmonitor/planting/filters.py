import django_filters
from .models import *
from django_filters import CharFilter


class PlannerFilter(django_filters.FilterSet):
    #valuechain = CharFilter(field_name="valuechain", lookup_expr='icontains')
    #title = CharFilter(field_name="title", lookup_expr='icontains')


    class Meta:
        model = PlantingDatePlannerC
        fields = ["vc_variety","ward","subcounty","county","valuechain"]
        fields = {
            
            'vc_variety': ['exact', ],
            'ward': ['exact', ],
            'subcounty': ['exact', ],
            'county': ['exact', ],
            'valuechain': ['exact', ]

        }