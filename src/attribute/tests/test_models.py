from django.test import TestCase
from attribute.models import Attribute, ProductAttribute
from category.models import Category
from product.models import Product
from django.contrib.auth import get_user_model

User = get_user_model()

class AttributeModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Elektronika')
        self.attribute = Attribute.objects.create(
            category_id=self.category,
            attribute_name='Rang',
            unit='N/A'
        )

    def test_attribute_creation(self):
        self.assertEqual(self.attribute.attribute_name, 'Rang')
        self.assertEqual(str(self.attribute), 'Rang')
        self.assertEqual(self.attribute.category_id.name, 'Elektronika')

class ProductAttributeModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Maishiy texnika')
        self.attribute = Attribute.objects.create(
            category_id=self.category,
            attribute_name='Hajmi',
            unit='Litr'
        )
        # User obyektini yaratish
        self.user = User.objects.create(
            username='testuser',
            password='testpass123',
            email='testuser@example.com',
            total_money=1000  # User modelida total_money majburiy
        )
        # Product obyektini yaratishda barcha majburiy maydonlarni to‘ldirish
        self.product = Product.objects.create(
            title='Muzlatkich',
            seller=self.user,
            price=5000000,  # Majburiy maydon
            description='Yangi muzlatkich',
            quantity=10,  # Majburiy maydon
            slug='muzlatkich-001'  # Majburiy maydon, unique bo‘lishi kerak
        )
        self.product_attribute = ProductAttribute.objects.create(
            product_id=self.product,
            attribute_id=self.attribute,
            value='300'
        )

    def test_product_attribute_creation(self):
        self.assertEqual(self.product_attribute.value, '300')
        self.assertEqual(str(self.product_attribute), '300')
        self.assertEqual(self.product_attribute.product_id.title, 'Muzlatkich')
        self.assertEqual(self.product_attribute.attribute_id.attribute_name, 'Hajmi')