from django.contrib import admin

from django.contrib import admin
from .models import Region

class SubRegionInline(admin.TabularInline):
    model = Region
    fk_name = 'parent_region'
    extra = 1
    show_change_link = True

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_region', 'add_region_at')
    list_filter = ('parent_region', 'add_region_at')
    search_fields = ('name',)
    readonly_fields = ('add_region_at',)
    inlines = [SubRegionInline]

    fieldsets = (
        (None, {
            'fields': ('name', 'parent_region')
        }),
        ('Qo‘shimcha ma’lumotlar', {
            'classes': ('collapse',),
            'fields': ('add_region_at',),
        }),
    )
