from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import User
from region.models import Region
from django.db import models


class UserAdmin(admin.ModelAdmin):
    # List display to show important fields in the list view
    list_display = ('username', 'role', 'status', 'total_money', 'region', 'phone')
    list_filter = ('status', 'role', 'region')  # Allow filtering by status, role, and region
    search_fields = ('username', 'phone')  # Allow searching by username and phone number
    ordering = ('-total_money',)  # Default ordering by total_money (descending)

    # Form layout for a more user-friendly display
    fieldsets = (
        (None, {
            'fields': ('username', 'password', 'first_name', 'last_name')
        }),
        (_('User Information'), {
            'fields': ('role', 'status', 'total_money', 'region', 'phone'),
        }),
    )

    # Ensure role choices are displayed clearly using the Select widget
    formfield_overrides = {
        models.CharField: {'widget': admin.widgets.AdminTextInputWidget(attrs={'size': 30})},
        models.SmallIntegerField: {'widget': admin.widgets.AdminRadioSelect()},
    }

    # Adding custom actions for batch updates
    actions = ['mark_active', 'mark_inactive']

    def mark_active(self, request, queryset):
        """Mark selected users as Active"""
        queryset.update(status=1)
        self.message_user(request, _("Selected users marked as Active"))

    def mark_inactive(self, request, queryset):
        """Mark selected users as Inactive"""
        queryset.update(status=0)
        self.message_user(request, _("Selected users marked as Inactive"))

    mark_active.short_description = _('Mark selected as Active')
    mark_inactive.short_description = _('Mark selected as Inactive')

    # Using custom widgets or a custom form for better UI if necessary
    # For instance, adding a custom widget for region selection could improve UX


# Register UserAdmin
admin.site.register(User, UserAdmin)
