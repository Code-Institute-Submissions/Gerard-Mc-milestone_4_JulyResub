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