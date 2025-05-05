from django.contrib import admin
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_category', 'add_category_at')
    list_filter = ('parent_category', 'add_category_at')
    search_fields = ('name',)
    ordering = ('name',)

    # Optional: shows nested categories in a clearer way
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('parent_category')

    # Optional: Better layout in the form
    fieldsets = (
        (None, {
            'fields': ('name', 'parent_category')
        }),
        ('Date Info', {
            'fields': ('add_category_at',),
            'classes': ('collapse',),  # collapsible section
        }),
    )
    readonly_fields = ('add_category_at',)
