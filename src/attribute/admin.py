from django.contrib import admin
from .models import Attribute, ProductAttribute

# 1) ProductAttribute uchun inline klass
class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute
    extra = 1           # yangi qiymat qo'shish uchun bo'sh satrlar soni
    fk_name = 'attribute_id'  # qaysi ForeignKey bo'yicha inline qilish

# 2) Attribute modeli uchun custom ModelAdmin
@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ('attribute_name', 'unit', 'category_id')  # ustunlar
    list_filter = ('category_id',)                            # filtr
    search_fields = ('attribute_name',)                       # qidiruv
    inlines = [ProductAttributeInline]                        # inline ro‘yxat

# 3) ProductAttribute alohida ro‘yxatga olinmaydi,
#    chunki uni Attribute ichida inline boshqaramiz.
