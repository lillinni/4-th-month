from django import forms
from . import models
from main_page.models import Book

class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = ['name', 'phone_number', 'email', 'book']
        widgets = {
            'book': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
