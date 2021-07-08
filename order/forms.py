from django import forms
from django.db import models 
from django.db.models import CharField, TextField
from portfolio.models import Product


class OrderForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'size', 'user_description', 'fast_delivery']
        labels = {
            'category': 'Type',
            'fast_delivery': '72 Hour Delivery +15%',
            'user_description': 'Description',
            'size': 'Size',
        }
        widgets = {
            'user_description': forms.Textarea(
                attrs={'placeholder': 'Your product\'s description...',
                'class': 'form-check-input w-100',
                'id': 'Description',
                }),
                'category': forms.Select(
                attrs={
                'class': 'form-check-input',
                'id': 'Type',
                }),
                'size': forms.Select(
                attrs={
                'class': 'form-check-input',
                'id': 'Size',
                }),
                'fast_delivery': forms.Select(
                attrs={
                'class': 'form-check-input',
                'id': 'Delivery',}),
        }
