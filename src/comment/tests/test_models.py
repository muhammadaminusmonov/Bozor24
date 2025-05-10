from django.test import TestCase
from django.contrib.auth import get_user_model
from product.models import Product
from comment.models import CommentProduct, CommentUser

User = get_user_model()

class CommentModelTests(TestCase):
    def setUp(self):
        
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.seller = User.objects.create_user(username='selleruser', password='testpass')

        self.product = Product.objects.create(name='Test Product', price=100)

    def test_create_comment_product(self):
        comment = CommentProduct.objects.create(
            user=self.user,
            text='This is a test comment for product.',
            product=self.product
        )
        self.assertEqual(str(comment), 'Product Comment: This is a test com')
        self.assertEqual(comment.product.name, 'Test Product')
        self.assertEqual(comment.user.username, 'testuser')

    def test_create_comment_user(self):
        comment = CommentUser.objects.create(
            user=self.user,
            text='This is a test comment for seller.',
            seller=self.seller
        )
        self.assertEqual(str(comment), 'User Comment: This is a test com')
        self.assertEqual(comment.seller.username, 'selleruser')
        self.assertEqual(comment.user.username, 'testuser')
