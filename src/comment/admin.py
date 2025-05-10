from django.contrib import admin
from .models import CommentProduct, CommentUser

class CommentProductInline(admin.TabularInline):
    model = CommentProduct
    extra = 0
    fields = ('user', 'text', 'writed_at')
    readonly_fields = ('user', 'text', 'writed_at')
    can_delete = False
    show_change_link = False

@admin.register(CommentProduct)
class CommentProductAdmin(admin.ModelAdmin):
    list_display = ('short_text', 'user', 'product', 'parent_comment_display', 'writed_at')
    list_filter = ('writed_at', 'product')
    search_fields = ('user__username', 'product__title', 'text')
    autocomplete_fields = ('user', 'product', 'parent_comment')
    readonly_fields = ('writed_at',)
    ordering = ('-writed_at',)

    fieldsets = (
        ('Comment Info', {
            'fields': ('user', 'product', 'text', 'writed_at')
        }),
        ('Reply to', {
            'fields': ('parent_comment',),
            'classes': ('collapse',),
        }),
    )

    def short_text(self, obj):
        return (obj.text[:75] + '...') if len(obj.text) > 75 else obj.text
    short_text.short_description = 'Comment'

    def parent_comment_display(self, obj):
        return obj.parent_comment.text[:50] + '...' if obj.parent_comment else "-"
    parent_comment_display.short_description = 'Reply to'

@admin.register(CommentUser)
class CommentUserAdmin(admin.ModelAdmin):
    list_display = ('seller',)
    search_fields = ('seller__username',)
    autocomplete_fields = ('seller',)
