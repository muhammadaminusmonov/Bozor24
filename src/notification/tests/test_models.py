# myapp/tests/test_models.py

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from notification.models import Follow, Notification
from product.models import Product  # kerakli joydan import qiling

User = get_user_model()

class FollowModelTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='alice', password='pass')
        self.user2 = User.objects.create_user(username='bob', password='pass')

    def test_create_follow(self):
        """Follower va followed munosabatini yaratish"""
        follow = Follow.objects.create(follower=self.user1, followed=self.user2)
        self.assertEqual(follow.follower, self.user1)
        self.assertEqual(follow.followed, self.user2)
        self.assertIsNotNone(follow.created_at)

    def test_unique_constraint(self):
        """Bir xil juftlik uchun faqat bitta follow bo‘lishi kerak"""
        Follow.objects.create(follower=self.user1, followed=self.user2)
        with self.assertRaises(IntegrityError):
            Follow.objects.create(follower=self.user1, followed=self.user2)

    def test_cascade_delete_user(self):
        """Foydalanuvchi o‘chirilsa, unga oid follow yozuvlari ham o‘chiriladi"""
        follow = Follow.objects.create(follower=self.user1, followed=self.user2)
        self.user1.delete()
        self.assertFalse(Follow.objects.filter(pk=follow.pk).exists())

    def test_related_name(self):
        """related_name orqali munosabatlar to‘g‘ri ishlashini tekshirish"""
        Follow.objects.create(follower=self.user1, followed=self.user2)
        self.assertIn(self.user2, [f.followed for f in self.user1.following.all()])
        self.assertIn(self.user1, [f.follower for f in self.user2.followers.all()])


class NotificationModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='charlie', password='pass')
        self.product = Product.objects.create(name='Test Product', price=10)

    def test_create_notification_without_product(self):
        """Productsiz notification yaratish"""
        notif = Notification.objects.create(recipient=self.user, message='Salom')
        self.assertEqual(notif.recipient, self.user)
        self.assertEqual(notif.message, 'Salom')
        self.assertIsNone(notif.product)
        self.assertIsNotNone(notif.timestamp)

    def test_create_notification_with_product(self):
        """Product bilan notification yaratish"""
        notif = Notification.objects.create(
            recipient=self.user,
            message='Yangi mahsulot',
            product=self.product
        )
        self.assertEqual(notif.recipient, self.user)
        self.assertEqual(notif.message, 'Yangi mahsulot')
        self.assertEqual(notif.product, self.product)

    def test_ordering_index(self):
        """Notificationlar timestamp bo‘yicha teskari tartibda chiqsin"""
        notif1 = Notification.objects.create(recipient=self.user, message='Birinchi')
        notif2 = Notification.objects.create(recipient=self.user, message='Ikkinchi')
        notifications = Notification.objects.filter(recipient=self.user).order_by('-timestamp')
        self.assertEqual(notifications.first(), notif2)
