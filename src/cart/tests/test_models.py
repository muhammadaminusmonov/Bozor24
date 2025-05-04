from django.test import TestCase
from django.contrib.auth import get_user_model
from product.models import Product
from cart.models import Cart, CartItem

User = get_user_model()

class CartModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='password123'
        )
        self.cart = Cart.objects.create(user=self.user)

    def test_cart_creation(self):
        self.assertEqual(self.cart.user, self.user)
        self.assertIsNotNone(self.cart.created_at)
        self.assertEqual(str(self.cart), f"Cart {self.cart.id} - {self.user.username}")


class CartItemModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='password123'
        )
        self.cart = Cart.objects.create(user=self.user)
        self.product = Product.objects.create(
            title='Test Product',
            seller=self.user,
            price=10000,
            discount=0,
            quantity=10,
            status=True
        )
        self.cart_item = CartItem.objects.create(cart=self.cart, product=self.product)

    def test_cart_item_creation(self):
        self.assertEqual(self.cart_item.cart, self.cart)
        self.assertEqual(self.cart_item.product, self.product)
        self.assertIsNotNone(self.cart_item.added_at)
        self.assertEqual(
            str(self.cart_item),
            f"Item {self.product.title} in Cart {self.cart.id}"
        )
