from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings


class Category(models.Model):
    CATEGORY_OPTIONS =[
        ("logo",'Logo'),
        ('poster','Poster'),
        ('icon','Icon'),
        ('banner','Banner'),
    ]
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(null=False, blank=False, max_length=254, choices=CATEGORY_OPTIONS)
    friendly_name = models.CharField(default="default", max_length=254, null=True, blank=True)
    price = models.DecimalField(
        default=0, null=False, blank=False, max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

    def get_price(self):
        return self.price

    