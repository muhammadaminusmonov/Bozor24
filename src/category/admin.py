from django.contrib import admin
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_category', 'add_category_at')
    list_filter = ('add_category_at', 'parent_category')
    search_fields = ('name',)
    ordering = ('-add_category_at',)
    autocomplete_fields = ('parent_category',)
    readonly_fields = ('add_category_at',)

    fieldsets = (
        (None, {
            'fields': ('name', 'parent_category')
        }),
        ('Timestamps', {
            'fields': ('add_category_at',),
            'classes': ('collapse',)
        }),
    )

    def get_queryset(self, request):
        # Prefetch for performance in admin
        return super().get_queryset(request).select_related('parent_category')
