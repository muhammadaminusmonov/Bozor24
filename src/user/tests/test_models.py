from user.models import User
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

