from django.test import TestCase
from user.models import User  # User modelini to'g'ri import qilish
from cart.models import Cart, CartItem, Product

class CartAdminTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Avval user yaratish
        cls.user = User.objects.create_user(username='testuser', password='12345')

        # Cart yaratish
        cls.cart = Cart.objects.create(user=cls.user)

        # Product yaratish, price va quantity maydonlarini to'ldirish
        cls.product = Product.objects.create(
            title="Product 1",
            price=100.0,  # price qo'shildi
            quantity=10   # quantity qo'shildi
        )

        # CartItem yaratish
        cls.cart_item = CartItem.objects.create(cart=cls.cart, product=cls.product, added_at="2025-05-01")



