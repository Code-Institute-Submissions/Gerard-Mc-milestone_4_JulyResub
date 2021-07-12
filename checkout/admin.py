from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    fields = ('order','type','complexity', 'variations', 
    'fast_delivery', 'user_description',
    'lineitem_total', 'is_complete')
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
    readonly_fields = ('order_number', 'date',
                       'grand_total')

    fields = ('order_number','date','grand_total')

    list_display = ('order_number', 'date', 'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)