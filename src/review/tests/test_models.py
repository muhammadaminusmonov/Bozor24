from django.core.exceptions import ValidationError
from django.test import TestCase
from django.contrib.auth import get_user_model
from product.models import Product
from review.models import Review
from region.models import Region
from category.models import Category

User = get_user_model()

class ReviewModelTest(TestCase):
    def setUp(self):
        self.region = Region.objects.create(name="Test Region")
        self.category = Category.objects.create(name="Test Category")
        self.user = User.objects.create_user(username='testuser', password='password123', region=self.region)
        self.product = Product.objects.create(
            title='Test Product',
            seller=self.user,
            price=10000,
            quantity=10,
            description='Test Description',
            category=self.category,
            region=self.region,
            slug='test-product'
        )

    def test_review_creation(self):
        review = Review.objects.create(
            product=self.product,
            user=self.user,
            rating=5
        )
        self.assertEqual(review.product, self.product)
        self.assertEqual(review.user, self.user)
        self.assertEqual(review.rating, 5)
        self.assertEqual(str(review), f"{self.user}  {self.product}  5")

    def test_review_rating_validation(self):
        review = Review(
            product=self.product,
            user=self.user,
            rating=6
        )
        # explicit validation
        with self.assertRaises(ValidationError):
            review.full_clean()

