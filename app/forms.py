from django import forms
from .models import Parcel

class ParcelForm(forms.ModelForm):
    class Meta:
        model = Parcel
        fields = [
            'name_article', 
            'description', 
            'value',
            'weight',
        ]
