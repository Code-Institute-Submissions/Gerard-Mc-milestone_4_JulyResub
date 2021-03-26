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
    name = models.CharField(max_length=254)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(
        null=True, blank=True, max_digits=6, decimal_places=2)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    user_description = models.TextField(null=False, blank=False)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    size = models.IntegerField(
        validators=[MinValueValidator(2), MaxValueValidator(4)])
    testimonial = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
