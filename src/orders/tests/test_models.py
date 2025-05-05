
from django.test import TestCase
from django.contrib.auth import get_user_model
from orders.models import Order, OrderItem
from product.models import Product

User = get_user_model()

class OrderModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="ali", password="1234")
        self.product = Product.objects.create(title="Kitob", price=50000)
        self.order = Order.objects.create(
            user=self.user,
            total_price=150000,
            status=1,
            payment_method="1",
            customer_address="Toshkent"
        )
        self.order_item = OrderItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=3,
            price_at_purchase=50000
        )

    def test_order_str(self):
        self.assertEqual(str(self.order), "ali")

    def test_order_item_str(self):
        expected = f"{self.order}, {self.product.title}"
        self.assertEqual(str(self.order_item), expected)

    def test_order_fields(self):
        self.assertEqual(self.order.total_price, 150000)
        self.assertEqual(self.order.status, 1)
        self.assertEqual(self.order.payment_method, "1")
        self.assertFalse(self.order.is_paid)
        self.assertFalse(self.order.is_released)

    def test_order_item_fields(self):
        self.assertEqual(self.order_item.quantity, 3)
        self.assertEqual(self.order_item.price_at_purchase, 50000)
        self.assertEqual(self.order_item.order, self.order)
