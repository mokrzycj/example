# forms.py w aplikacji clinics

from django import forms
from .models import Clinic, ClinicRequest

class ClinicForm(forms.ModelForm):
    class Meta:
        model = Clinic
        fields = ['name', 'address', 'phone_number', 'email']

class ClinicRequestForm(forms.ModelForm):
    class Meta:
        model = ClinicRequest
        fields = ['status']
