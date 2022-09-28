from django import forms

from .models import MyFarm




class RegisterFarmForm(forms.ModelForm):
    #first_name = forms.CharField(max_length=255)
    #last_name = forms.CharField(max_length=255)
    #email = forms.EmailField()

    class Meta:
        model = MyFarm
        fields = '__all__'
        exclude = ['user']


def form_validation_error(form):
    msg = ""
    for field in form:
        for error in field.errors:
            msg += "%s: %s \\n" % (field.label if hasattr(field, 'label') else 'Error', error)
    return msg


"""class RegisterFarmForm(forms.ModelForm):
   
    class Meta:
        model = MyFarm
        fields = "__all__"
        
        
        
        
    [
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
        """
