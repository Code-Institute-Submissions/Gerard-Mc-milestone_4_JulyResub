import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from portfolio.models import Category
from decimal import Decimal


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_order_number(self):
        return uuid.uuid4().hex.upper()

    def update_total(self):
        self.grand_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum']
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
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
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(null=True, max_length=254)
    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.SET_NULL)
    complexity = models.DecimalField(
        default=1,max_digits=3, decimal_places=2, choices=COMPLEXITY_OPTIONS)
    variations = models.DecimalField(default=1,max_digits=3, decimal_places=2, choices=VARIATION_CHOICES)
    user_description = models.TextField(default="", null=False, blank=False)
    fast_delivery  = models.BooleanField(default=False, null=True, blank=True, choices=DELIVERY_CHOICES)
    is_complete = models.BooleanField(default=False, null=True, blank=True)
    lineitem_total = models.DecimalField(default=0, max_digits=10, decimal_places=2,null=False, blank=False, editable=False)
    order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.CASCADE, related_name='lineitems')
    type = models.DecimalField(default=1, max_digits=3, decimal_places=1, choices=CATEGORY_OPTIONS)

    def save(self, *args, **kwargs):
        category_pk = Decimal(self.type)
        item = Category.objects.get(pk=category_pk)
        delivery = 1
        if self.fast_delivery == True:
            delivery = Decimal(settings.FAST_DELIVERY_CHARGE)

        self.lineitem_total = Decimal(item.price * self.complexity * self.variations * delivery)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Name {self.type} on order {self.order.order_number}'

