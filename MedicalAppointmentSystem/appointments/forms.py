# forms.py w aplikacji appointments

from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['specialist', 'scheduled_time']
