from django.contrib import admin
from .models import Product, ProductImage, PromotedProduct
from django.utils.html import format_html

# Inline for ProductImage
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

# Inline for PromotedProduct
class PromotedProductInline(admin.StackedInline):
    model = PromotedProduct
    extra = 0
    max_num = 1  # one product -> one promotion
    can_delete = True

    def get_queryset(self, request):
        # Prevent showing irrelevant entries
        return super().get_queryset(request).select_related('product', 'user')

# Main Product admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'seller', 'price', 'quantity', 'status', 'view_count', 'created_at')
    list_filter = ('status', 'category', 'region', 'created_at')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProductImageInline, PromotedProductInline]

    fieldsets = (
        (None, {
            'fields': ('seller', 'title', 'slug', 'description', 'price', 'quantity', 'status')
        }),
        ('Discount Info', {
            'fields': ('discount', 'discount_limit_date')
        }),
        ('Classification', {
            'fields': ('category', 'region')
        }),
    )
