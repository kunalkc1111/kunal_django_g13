from django import forms
from .models import FillDetailsModels

class FillDetailsForm(forms.ModelForm):
    class Meta:
        model = FillDetailsModels
        fields = '__all__'