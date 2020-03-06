from django import forms
from .models import DoctorLeave

class LeaveForm(forms.ModelForm):
    fromname=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','size':20}))
    to=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','size':20}))
    department=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','size':20}))
    date=forms.CharField(widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))
    reason=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','size':20}))
    
    class Meta:
        model=DoctorLeave
        fields=['fromname','to','department','date','reason']