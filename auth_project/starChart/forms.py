from django import forms
from .models import starSighting

class starSightingForm(forms.ModelForm):
    class Meta:
        model = starSighting
        fields = ['star_name', 'date_seen']
        widgets = {
            'date_seen': forms.DateInput(attrs={'type': 'date'}),
        }