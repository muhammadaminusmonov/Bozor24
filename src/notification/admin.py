from django.contrib import admin
from .models import Follow, Notification




@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'recipient', 'message', 'product', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('recipient__username', 'message', 'product__name')
    ordering = ('-timestamp',)
