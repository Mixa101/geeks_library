from django import forms
from .models import Order

class BacketForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'phone_number', 'email', 'book']
