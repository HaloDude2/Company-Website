from django import forms
from .models import Apointment

class AppointmentForm(forms.ModelForm):
    date = forms.DateTimeField(imput_formats=['%d/%m/%Y %H:%M'])

    class Meta:
        model = Appointment
        fields = ('__all__')