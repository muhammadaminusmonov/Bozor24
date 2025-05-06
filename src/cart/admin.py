from django.contrib import admin
from .models import Cart, CartItem

# 1. CartItem uchun Inline klass
class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0                  # Bo‘sh yangi satrlar soni
    fields = ('product', 'quantity', 'added_at')
    readonly_fields = ('added_at',)

# 2. Faqat bitta Admin: CartAdmin ichida inline sifatida CartItemInline
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username',)
    inlines = [CartItemInline]  # <-- bu yerda birlashtiramiz

# (3. agar avval CartItemAdmin ro‘yxatdan o‘tgan bo‘lsa, uni olib tashlang)
# admin.site.unregister(CartItem)
