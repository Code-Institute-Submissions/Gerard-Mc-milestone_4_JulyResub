from django import forms
from django.db import models 
from django.db.models import CharField, TextField
from portfolio.models import Product



class CustomProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'complexity', 'variations', 'user_description', 'fast_delivery']
        labels = {
            'category': 'Type',
            'variations': 'Variations',
            'complexity': 'Complexity',
            'fast_delivery': '72 Hour Delivery +15%',
            'user_description': 'Description',
        }
        widgets = {
            'user_description': forms.Textarea(
                attrs={'placeholder': 'Your product\'s description...',
                'class': 'form-check-input w-100',
                'style': 'max-height: 100px',
                'id': 'Description',
                }),
                'category': forms.Select(
                attrs={
                'onclick': 'total()',
                'class': 'form-check-input',
                'id': 'item_type',
                'required':True
                }),
                'complexity': forms.Select(
                attrs={
                'onclick': 'total()',
                'class': 'form-check-input',
                'id': 'complexity',
                }),
                'variations': forms.Select(
                attrs={
                'onclick': 'total()',
                'class': 'form-check-input',
                'id': 'variations',
                }),
                'fast_delivery': forms.Select(
                attrs={
                'onclick': 'total()',
                'class': 'form-check-input',
                'id': 'delivery',
                }),
        }


