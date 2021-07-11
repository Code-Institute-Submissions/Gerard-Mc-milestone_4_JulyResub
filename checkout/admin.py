from django.contrib import admin
from .models import Order
from portfolio.models import Product


class ProductAdminInline(admin.TabularInline):
    model = Product
    fields = ('order','category','complexity', 'variations', 
    'fast_delivery', 'user_description',
    'price_total', 'is_complete')
    readonly_fields = ('price_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (ProductAdminInline,)
    readonly_fields = ('order_number', 'date',
                       'grand_total')

    fields = ('order_number','date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county','grand_total')

    list_display = ('order_number', 'date', 'full_name','grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)