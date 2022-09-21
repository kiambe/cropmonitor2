from rest_framework import serializers
from planting.models import *

class PlantingSerializer(serializers.ModelSerializer):
    value_chain_name = serializers.ReadOnlyField(
        source="valuechain.name"
    )
    county_name = serializers.ReadOnlyField(
        source='county.name')
    subcounty_name = serializers.ReadOnlyField(
        source='subcounty.name')
    ward_name = serializers.ReadOnlyField(
        source='ward.name')
    class Meta:
        model = PlantingDatePlannerC
        # fields = "__all__"
        # depth = 1
        fields=["min_maturity_period","max_maturity_period","first_weeding_after_days","second_weeding_after_days",
                "ferlizer_application_recommendation","min_expected_yield","max_expected_yield",
                "areas_for_optimal_production","special_attributes","sow_end_date","sow_start_date","refyear",
                "vc_variety","valuechain","ward","subcounty","county","value_chain_name",'county_name','subcounty_name','ward_name'
                ]