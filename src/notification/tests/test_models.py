from django.test import TestCase
from django.contrib.auth import get_user_model
from product.models import Product
from notification.models import Follow, Notification
from django.db.utils import IntegrityError

User = get_user_model()

class FollowModelTest(TestCase):
    def setUp(self):
        # Create two users for follow relationship
        self.user1 = User.objects.create_user(username="testuser1", password="password1")
        self.user2 = User.objects.create_user(username="testuser2", password="password2")

    def test_create_follow(self):
        # User1 follows User2
        follow = Follow.objects.create(follower=self.user1, followed=self.user2)
        self.assertEqual(follow.follower, self.user1)
        self.assertEqual(follow.followed, self.user2)

    def test_unique_follow_constraint(self):
        # Ensure the same user cannot follow the same person twice
        Follow.objects.create(follower=self.user1, followed=self.user2)
        with self.assertRaises(IntegrityError):
            Follow.objects.create(follower=self.user1, followed=self.user2)

    def test_created_at_field(self):
        # Ensure that the `created_at` field is set when the follow relationship is created
        follow = Follow.objects.create(follower=self.user1, followed=self.user2)
        self.assertIsNotNone(follow.created_at)

class NotificationModelTest(TestCase):
    def setUp(self):
        # Create a user and a product for the notification
        self.user = User.objects.create_user(username="testuser", password="password")
        self.product = Product.objects.create(title="Test Product", price=100.0)

    def test_create_notification(self):
        # Create a notification for a user related to a product
        notification = Notification.objects.create(
            recipient=self.user,
            message="You have a new follow!",
            product=self.product
        )

        self.assertEqual(notification.recipient, self.user)
        self.assertEqual(notification.message, "You have a new follow!")
        self.assertEqual(notification.product, self.product)

    def test_timestamp_field(self):
        # Ensure that the `timestamp` field is set automatically when the notification is created
        notification = Notification.objects.create(
            recipient=self.user,
            message="You have a new follow!",
            product=self.product
        )
        self.assertIsNotNone(notification.timestamp)
