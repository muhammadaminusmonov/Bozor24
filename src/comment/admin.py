from django.contrib import admin
from .models import CommentProduct, CommentUser

@admin.register(CommentProduct)
class CommentProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'text', 'writed_at', 'parent_comment')
    search_fields = ('user__username', 'product__name', 'text')
    list_filter = ('writed_at',)
    ordering = ('-writed_at',)

@admin.register(CommentUser)
class CommentUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'seller')
    search_fields = ('seller__username',)
