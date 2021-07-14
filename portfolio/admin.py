from django.contrib import admin
from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'category',
        'complexity',
        'lineitem_total',
        'is_complete',
        'display_in_portfolio',
    )

    ordering = ('is_complete',)


admin.site.register(Product, ProductAdmin)