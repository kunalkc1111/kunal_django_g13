from django import forms
from .models import FillDetailsModels, SignUpModel

class FillDetailsForm(forms.ModelForm):
    class Meta:
        model = FillDetailsModels
        fields = '__all__'

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUpModel
        fields = '__all__'