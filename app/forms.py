from django import forms
from .models import Parcel

class ParcelForm(forms.ModelForm):
    class Meta:
        model = Parcel
        fields = [
            'tracking_number', 
            'adress_dep', 
            'adress_arr',
            'weight',
        ]
