from django import forms
from .models import Customuser

Type_choices=(('Doctor','Doctor'),
    ('Patient','Patient'),
    ('Admin','Admin'),
     )
class RegistrationForm(forms.ModelForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    type=forms.CharField(widget=forms.Select(choices=Type_choices,attrs={'class':'form-control'}))
    class Meta:
        model=Customuser
        fields=['email','username','password','type']

class LoginForm(forms.Form):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))