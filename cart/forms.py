from django import forms
from django.forms.fields import CharField

from django.core.validators import RegexValidator

class CheckoutForm(forms.Form):
    first_name = forms.CharField(max_length=255, validators=[RegexValidator(r'^[a-zA-Z]*$', ' only alphabet characters are allowed.')])
    last_name = forms.CharField(max_length=255, validators=[RegexValidator(r'^[a-zA-Z]*$', ' only alphabet characters are allowed.')])
    email = forms.EmailField(max_length=255)
    phone = forms.CharField(max_length=10, min_length=10, validators=[RegexValidator(r'^[0-9+]', 'Only digit characters.')])
    address = forms.CharField(max_length=255)
    zipcode = forms.CharField(max_length=6, min_length=6, validators=[RegexValidator(r'^[0-9+]', 'Only digit characters.')])
    place = forms.CharField(max_length=255)
    stripe_token = forms.CharField(max_length=255)


    
