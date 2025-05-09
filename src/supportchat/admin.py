from django.contrib import admin
from .models import SupportChatRoom, SupportMessage

@admin.register(SupportChatRoom)
class SupportChatRoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at')
    search_fields = ('user__username',)


@admin.register(SupportMessage)
class SupportMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'room', 'sender', 'sent_at')
    search_fields = ('sender__username', 'message')
    list_filter = ('sent_at',)
