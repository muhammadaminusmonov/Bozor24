from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.html import format_html
from .models import User, Follow


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        'username', 'email', 'phone', 'role', 'status_display', 'region', 'total_money', 'date_joined'
    )
    list_filter = ('role', 'status', 'region', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'phone')
    ordering = ('-date_joined',)
    readonly_fields = ('date_joined', 'last_login')
    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'phone', 'password')
        }),
        ('Personal Info', {
            'fields': ('first_name', 'last_name', 'region', 'role', 'status', 'total_money')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Important Dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )

    def status_display(self, obj):
        color = "green" if obj.status == 1 else "red"
        return format_html('<strong style="color:{};">{}</strong>', color, obj.get_status_display())
    status_display.short_description = 'Status'


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('follower_link', 'seller_link', 'follow_at')
    list_filter = ('follow_at',)
    search_fields = ('follower__username', 'seller__username')

    def follower_link(self, obj):
        return format_html('<a href="/admin/user/user/{}/change/">{}</a>', obj.follower.id, obj.follower.username)
    follower_link.short_description = 'Follower'

    def seller_link(self, obj):
        return format_html('<a href="/admin/user/user/{}/change/">{}</a>', obj.seller.id, obj.seller.username)
    seller_link.short_description = 'Seller'
