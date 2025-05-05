from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from product.models import Product, ProductImage, PromotedProduct
from region.models import Region
from category.models import Category
from datetime import timedelta

User = get_user_model()

class ProductModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.region = Region.objects.create(name='Tashkent')
        self.category = Category.objects.create(name='Electronics')

    def create_product(self):
        return Product.objects.create(
            title='Smartphone',
            slug='smartphone',
            seller=self.user,
            price=500000,
            discount=10,
            discount_limit_date=timezone.now() + timedelta(days=7),
            description='Great phone',
            quantity=10,
            category=self.category,
            region=self.region,
            status=True,
        )

    def test_product_creation(self):
        product = self.create_product()
        self.assertEqual(product.title, 'Smartphone')
        self.assertEqual(str(product), 'Smartphone')
        self.assertEqual(product.view_count, 0)
        self.assertTrue(product.status)

    def test_product_image_creation(self):
        product = self.create_product()
        image = ProductImage.objects.create(product=product, image='http://example.com/image1.jpg')
        self.assertEqual(image.product, product)
        self.assertIn('Image for', str(image))

    def test_promoted_product_creation(self):
        product = self.create_product()
        promo = PromotedProduct.objects.create(
            product=product,
            promo_type='1',  # must be a string because promo_type is CharField
            user=self.user,
            amount=10,
            status=1,
            view_limit=100
        )
        self.assertEqual(promo.product, product)
        self.assertEqual(promo.status, 1)
        self.assertEqual(promo.amount, 10)
