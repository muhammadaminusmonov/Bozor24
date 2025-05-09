from django.contrib import admin
from .models import SupportChatRoom, SupportMessage

class SupportMessageInline(admin.TabularInline):
    model = SupportMessage
    extra = 0
    readonly_fields = ('sender', 'message', 'sent_at')
    can_delete = False

@admin.register(SupportChatRoom)
class SupportChatRoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at')
    search_fields = ('user__username',)
    inlines = [SupportMessageInline]
