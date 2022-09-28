from django import forms

from .models import MyFarm


class RegisterFarmForm(forms.ModelForm):
   
    class Meta:
        model = MyFarm
        fields = [
            "farm_name",
            "slug",
            "valuechain",
            "vc_variety",
            "owner",
            "farm_ownership",
            "county",
            "subcounty",
            "ward",
            "lat",
            "lon",
            "farm_size_ha",
            "status",
        ]
        



