from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    SIZE_OPTIONS =[
        ('small', 'Small'),
        ('medium','Medium'),
        ('large','Large'),
    ]

    DELIVERY_OPTIONS =[
        ( True, 'Yes'),
        ( False,'No'),
    ]
    name = models.CharField(max_length=254)
    user_name = models.CharField(default='username', max_length=254)
    friendly_name = models.CharField(null=True, max_length=254)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(
        null=True, blank=True, max_digits=6, decimal_places=2)
    category = models.ForeignKey(
        'Category', null=True, blank=False, on_delete=models.SET_NULL)
    size = models.CharField(
        max_length=16, null=True,
        blank=False, choices=SIZE_OPTIONS)
    user_description = models.TextField(null=False, blank=False)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    testimonial = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/')
    complete = models.BooleanField(default=False, null=True, blank=True)
    fast_delivery = models.BooleanField(null=True, blank=False, choices=DELIVERY_OPTIONS)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
