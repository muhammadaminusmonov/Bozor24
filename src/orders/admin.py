# # orders/admin.py
# from django.contrib import admin
# from .models import Orders
#
# admin.site.register(Orders)

# orders/admin.py
from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'total_price', 'status', 'is_paid', 'is_released')
    list_filter = ('status', 'payment_method', 'is_paid', 'is_released')
    search_fields = ('user__username', 'customer_address')
    inlines = [OrderItemInline]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price_at_purchase')
    search_fields = ('product__title',)

