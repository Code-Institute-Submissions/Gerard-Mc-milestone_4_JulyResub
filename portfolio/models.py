SECRET_KEY="SDASDSFSDFGREGVICJVFDIPTGUERKMOVPK904U85T893YU6"







from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from decimal import Decimal
from django.conf import settings
from checkout.models import Order

CATEGORY_OPTIONS =[
        (1,'Logo'),
        (2,'Poster'),
        (3,'Icon'),
        (4,'Banner'),
    ]

VARIATION_CHOICES =[
    (1.00, 'Single'),
    (1.25,'2  (+25%)'),
    (1.50,'3  (+50%)'),
    (1.75,'3  (+75%)'),
    ]

DELIVERY_CHOICES =[
    (False, "No"),
    (True, "Yes"),
    ]

COMPLEXITY_OPTIONS =[
    (1.00, 'Normal'),
    (1.25,'Advanced (+25%)'),
    (1.50,'Complex (+50%)'),
]

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(null=False, blank=False, max_length=254, choices=CATEGORY_OPTIONS)
    friendly_name = models.CharField(default="default", max_length=254, null=True, blank=True)
    price = models.DecimalField(
        default=0, null=False, blank=False, max_digits=6, decimal_places=2)

    def __str__(self):
        return self.friendly_name

    def get_price(self):
        return self.price


class Product(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(null=True, max_length=254)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    complexity = models.DecimalField(
        default=1,max_digits=3, decimal_places=2, choices=COMPLEXITY_OPTIONS)
    variations = models.DecimalField(default=1,max_digits=3, decimal_places=2, choices=VARIATION_CHOICES)
    user_description = models.TextField(default="", null=False, blank=False)
    fast_delivery  = models.BooleanField(default=False, null=True, blank=True, choices=DELIVERY_CHOICES)
    is_complete = models.BooleanField(default=False, null=True, blank=True)
    price_total = models.DecimalField(default=0, max_digits=10, decimal_places=2,null=False, blank=False, editable=False)
    order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.CASCADE, related_name='lineitems')
    type = models.DecimalField(default=1, max_digits=3, decimal_places=1, choices=CATEGORY_OPTIONS)

    def save(self, *args, **kwargs):
        delivery = 1
        if self.fast_delivery == True:
            delivery = Decimal(settings.FAST_DELIVERY_CHARGE)

        self.price_total = self.category.price * self.complexity * self.variations * delivery
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Name {self.type} on order {self.order.order_number}'

    