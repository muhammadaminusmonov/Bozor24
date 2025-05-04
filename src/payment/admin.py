from django.contrib import admin
from .models import Payment, Transaction


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'amount', 'method', 'payment_at')
    list_filter = ('method', 'payment_at')
    search_fields = ('user__username', 'user__email', 'amount')
    ordering = ('-payment_at',)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'buyer', 'amount', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('order__id', 'buyer__user__username', 'amount')
    ordering = ('-created_at',)
