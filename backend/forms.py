from django.forms import ModelForm
from django import forms
from .models import  Contact

        
class ContactForm(ModelForm):    
    class Meta:
        model = Contact
        fields = ('name', 'address', 'email_address' , 'phone', 'web','zip_code') 
        labels = {
            'name': '',
            'address': '',
            'email_address': '',
            'phone': '',
            'web': '',
            'zip_code': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),
            'address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}),
            'email_address': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
            'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}),
            'web': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Web Address'}),
            'zip_code': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zip Code'}),
        }
        
        
        


