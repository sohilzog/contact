from django import forms
from django.contrib.auth.models import User
from .models import Contact


class ContactRegisterForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phnno']
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "name"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "email"}),
            "phnno": forms.TextInput(attrs={"class": "form-control", "placeholder": "number"}),
        }
