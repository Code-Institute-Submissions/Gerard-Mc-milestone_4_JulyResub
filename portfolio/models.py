from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from checkout.models import OrderLineItem, Category


class Product(models.Model):
    DISPLAY_OPTIONS =[
        ( True, 'Yes'),
        ( False,'No'),
    ]

    OrderLineItem = models.ForeignKey(
        OrderLineItem , null=True, blank=False, on_delete=models.SET_NULL)
    display_in_portfolio = models.BooleanField(default=False, null=True, blank=True, choices=DISPLAY_OPTIONS)
    name = models.CharField(default="", null=True, blank=True, max_length=254)
    friendly_name = models.CharField(default="", null=True, blank=True, max_length=254)
    category = models.CharField(default="", null=True, blank=True, max_length=254)
    complexity = models.DecimalField(
        default=1,max_digits=3, decimal_places=2, null=True, blank=True)
    variations = models.DecimalField(default=1,max_digits=3, decimal_places=2, null=True, blank=True)
    user_description = models.TextField(default="", null=True, blank=True)
    is_complete = models.BooleanField(default=False, null=True, blank=True)
    lineitem_total = models.DecimalField(default=0, max_digits=10, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        self.name = self.OrderLineItem.name
        self.friendly_name = self.OrderLineItem.friendly_name
        self.category = self.OrderLineItem.category.name
        self.complexity = self.OrderLineItem.complexity
        self.variations = self.OrderLineItem.variations
        self.user_description = self.OrderLineItem.user_description
        self.is_complete = self.OrderLineItem.is_complete
        self.lineitem_total = self.OrderLineItem.lineitem_total
        super().save(*args, **kwargs)

    def __str__(self):
        return self.OrderLineItem.friendly_name
