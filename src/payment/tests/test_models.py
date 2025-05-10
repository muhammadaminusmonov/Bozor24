from django.test import TestCase
from payment.models import Payment, Transaction
from orders.models import Order
from user.models import User
from region.models import Region


class PaymentTransactionTestCase(TestCase):
    def setUp(self):
        self.region = Region.objects.create(name="Test Region")

        self.user = User.objects.create_user(
            username="testuser",
            password="password123",
            region=self.region
        )

        self.order = Order.objects.create(user=self.user, total_price=150000)

        self.payment = Payment.objects.create(
            user=self.user,
            amount=150000,
            method='1'  # string formatda bo'lishi kerak
        )

        self.transaction = Transaction.objects.create(
            order=self.order,
            buyer=self.user,
            amount=150000,
            status=1
        )

    def test_payment_created(self):
        self.assertEqual(self.payment.user, self.user)
        self.assertEqual(self.payment.amount, 150000)
        self.assertEqual(self.payment.method, '1')  # string bo'lishi kerak

    def test_transaction_created(self):
        self.assertEqual(self.transaction.order, self.order)
        self.assertEqual(self.transaction.buyer, self.user)
        self.assertEqual(self.transaction.amount, 150000)
        self.assertEqual(self.transaction.status, 1)

    def test_str_methods(self):
        self.assertEqual(str(self.payment), "150000")
        self.assertEqual(str(self.transaction), "150000")
