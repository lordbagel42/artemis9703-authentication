# custom login screen

from django import forms

class ImageLoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    image = forms.ImageField()

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=255)
    image = forms.ImageField()