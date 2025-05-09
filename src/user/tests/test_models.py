from django.utils import timezone
from user.models import User, Follow
from django.test import TestCase
from region.models import Region

class UserModelTest(TestCase):

    def setUp(self):
        self.region = Region.objects.create(name='Toshkent')

    def test_user_creation(self):
        user = User.objects.create_user(
            username='testuser',
            password='password123',
            region=self.region,
            status=1,
            role='user',
            total_money=10000
        )

        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.check_password('password123'))
        self.assertEqual(user.status, 1)
        self.assertEqual(user.role, 'user')
        self.assertEqual(user.total_money, 10000)
        self.assertEqual(user.region.name, 'Toshkent')

    def test_user_str_method(self):
        user = User.objects.create_user(
            username='testuser',
            password='password456',
            region=self.region
        )
        self.assertEqual(str(user), 'testuser')


class FollowModelTest(TestCase):

    def setUp(self):
        self.follower = User.objects.create_user(username='buyer', password='testpass123')
        self.seller = User.objects.create_user(username='seller', password='testpass123')

    def test_follow_creation(self):
        follow = Follow.objects.create(follower=self.follower, seller=self.seller)

        self.assertEqual(follow.follower, self.follower)
        self.assertEqual(follow.seller, self.seller)
        self.assertIsNotNone(follow.follow_at)
        self.assertTrue(timezone.now() - follow.follow_at < timezone.timedelta(seconds=5))

    def test_follow_str(self):
        follow = Follow.objects.create(follower=self.follower, seller=self.seller)
        expected = f"{self.follower.username} follows {self.seller.username}"
        self.assertEqual(str(follow), expected)