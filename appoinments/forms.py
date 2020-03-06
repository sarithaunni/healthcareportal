from django import forms
from .models import Appoinment

class AppoinmentForm(forms.ModelForm):
    appoinmentdate=forms.CharField(widget=forms.DateInput(attrs={'type':'datetime-local'}))

    class Meta:
        model=Appoinment
        exclude=['user','status']

class UpdateAppoinmentForm(forms.ModelForm):
    appoinmentdate=forms.CharField(widget=forms.DateInput(attrs={'type':'datetime-local'}))

    class Meta:
        model=Appoinment
        exclude=['user']