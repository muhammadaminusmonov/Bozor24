from django.test import TestCase
from django.contrib.auth import get_user_model
from supportchat.models import SupportChatRoom, SupportMessage

User = get_user_model()

class SupportModelsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user1', password='testpass')
        self.admin = User.objects.create_user(username='admin1', password='adminpass', is_staff=True)
        self.chat_room = SupportChatRoom.objects.create(user=self.user)

    def test_support_chat_room_creation(self):
        self.assertEqual(SupportChatRoom.objects.count(), 1)
        self.assertEqual(self.chat_room.user, self.user)
        self.assertIn("Support Chat Room", str(self.chat_room))

    def test_support_message_creation_by_user(self):
        message = SupportMessage.objects.create(
            room=self.chat_room,
            sender=self.user,
            message="Hello, I need help."
        )
        self.assertEqual(SupportMessage.objects.count(), 1)
        self.assertEqual(message.room, self.chat_room)
        self.assertEqual(message.sender, self.user)
        self.assertIn("Hello", message.message)
        self.assertIn(self.user.username, str(message))

    def test_support_message_creation_by_admin(self):
        message = SupportMessage.objects.create(
            room=self.chat_room,
            sender=self.admin,
            message="We are here to help you!"
        )
        self.assertEqual(message.sender, self.admin)
        self.assertTrue(self.admin.is_staff)
