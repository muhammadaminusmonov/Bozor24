from django.test import TestCase
from comment.models import CommentProduct  # Sizning model joylashgan joyga mos ravishda import qilish
from django.db.utils import IntegrityError

class CommentProductTest(TestCase):
    def test_create_comment(self):
        # To'g'ri comment yaratish
        comment = CommentProduct.objects.create(
            text="This is a test comment",
            product_name="Test Product",
            user="testuser"  # yoki test foydalanuvchi ob'ekti
        )

        self.assertEqual(comment.text, "This is a test comment")
        self.assertEqual(comment.product_name, "Test Product")
        self.assertEqual(comment.user.username, "testuser")

    def test_empty_comment_text(self):
        # Bo'sh comment matnini qo'yish
        with self.assertRaises(IntegrityError):
            CommentProduct.objects.create(
                text="",
                product_name="Test Product",
                user="testuser"
            )

    def test_ordering_of_comments(self):
        # Bir nechta commentlarni yaratish va to'g'ri tartibda olish
        comment1 = CommentProduct.objects.create(
            text="First comment",
            product_name="Test Product",
            user="testuser"
        )
        comment2 = CommentProduct.objects.create(
            text="Second comment",
            product_name="Test Product",
            user="testuser"
        )

        comments = CommentProduct.objects.all().order_by(
            '-created_at')  # 'created_at' modelga moslashtirilgan vaqt maydoni
        self.assertEqual(list(comments), [comment2, comment1])
