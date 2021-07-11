from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from decimal import Decimal


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    CATEGORY_OPTIONS =[
        (1, 'Logo'),
        (2,'Poster'),
        (3,'Icon'),
        (4,'Banner'),
    ]

    name = models.CharField(null=False, blank=False, max_length=254, choices=CATEGORY_OPTIONS)
    price = models.DecimalField(
        default=0, null=False, blank=False, max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

    def get_price(self):
        return self.price


class Product(models.Model):

    
    VARIATION_CHOICES =[
        (1, '1'),
        (2,'2  (+20%)'),
        (3,'3  (+35%)'),
        (4,'4  (+45%)'),
        ]

    DELIVERY_CHOICES =[
        (False, "No"),
        (True, "Yes"),
        ]

    COMPLEXITY_OPTIONS =[
        (1.00, 'Normal'),
        (1.25,'Advanced  (+25%)'),
        (1.50,'Complex  (+50%)'),
    ]


    name = models.CharField(max_length=254)
    friendly_name = models.CharField(null=True, max_length=254)
    category = models.ForeignKey(
        'Category', null=True, blank=False, on_delete=models.SET_NULL)
    complexity = models.DecimalField(
        default=1,max_digits=3, decimal_places=2, choices=COMPLEXITY_OPTIONS)
    variations = models.DecimalField(default=1, max_digits=1, decimal_places=0, choices=VARIATION_CHOICES)
    user_description = models.TextField(default="", null=False, blank=False)
    fast_delivery  = models.BooleanField(default=False, null=True, blank=True, choices=DELIVERY_CHOICES)
    is_complete = models.BooleanField(default=False, null=True, blank=True)
        

    def __str__(self):
        return self.name

    