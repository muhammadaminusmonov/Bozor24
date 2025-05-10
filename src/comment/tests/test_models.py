from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.db import IntegrityError
from comment.models import CommentProduct, CommentUser
from product.models import Product
from category.models import Category
from region.models import Region

User = get_user_model()

class CommentModelsTest(TestCase):
    def setUp(self):
        # Test uchun Category va Region yaratish
        self.category = Category.objects.create(name='Test Category')
        self.region = Region.objects.create(name='Test Region')

        # Foydalanuvchilarni yaratish
        self.user = User.objects.create_user(
            username='testuser', email='test@example.com', password='pass'
        )
        self.other_user = User.objects.create_user(
            username='seller', email='seller@example.com', password='pass'
        )

        # Mahsulotni yaratish
        self.product = Product.objects.create(
            title='Test Product',
            seller=self.user,
            price=100,
            discount=None,
            discount_limit_date=None,
            description='Test Description',
            quantity=10,
            category=self.category,
            region=self.region,
            slug='test-product'
        )

    def test_commentproduct_creation_and_str(self):
        # CommentProduct yaratish
        comment = CommentProduct.objects.create(
            user=self.user,
            product=self.product,
            text='Bu mahsulot juda yaxshi!',
        )
        # Tekshiruvlar
        self.assertEqual(comment.user, self.user)
        self.assertEqual(comment.product, self.product)
        self.assertEqual(comment.text, 'Bu mahsulot juda yaxshi!')
        now = timezone.now()
        self.assertTrue((now - comment.writed_at).total_seconds() < 5)
        expected_str = f"Comment by {self.user.username} on {self.product.title}"
        self.assertEqual(str(comment), expected_str)

    def test_commentproduct_default_parent(self):
        # Default bo‘sh parent_comment
        comment = CommentProduct.objects.create(
            user=self.user,
            product=self.product,
            text='No parent comment'
        )
        self.assertIsNone(comment.parent_comment)

    def test_commentproduct_empty_text(self):
        # Bo‘sh matnni saqlashda IntegrityError ni tekshirish
        with self.assertRaises(IntegrityError):
            CommentProduct.objects.create(
                user=self.user,
                product=self.product,
                text=''
            )

    def test_commentproduct_ordering(self):
        # Izohlarni vaqt tartibida tekshirish
        comment1 = CommentProduct.objects.create(user=self.user, product=self.product, text='First')
        comment2 = CommentProduct.objects.create(user=self.user, product=self.product, text='Second')
        comments = CommentProduct.objects.filter(product=self.product).order_by('-writed_at')
        self.assertEqual(list(comments), [comment2, comment1])

    def test_commentproduct_verbose_name(self):
        # Verbose name tekshirish
        field = CommentProduct._meta.get_field('text')
        self.assertEqual(field.verbose_name, 'text')

    def test_commentproduct_parent(self):
        parent = CommentProduct.objects.create(
            user=self.user, product=self.product, text='Bosh izoh'
        )
        child = CommentProduct.objects.create(
            user=self.other_user,
            product=self.product,
            text='Javob izoh',
            parent_comment=parent
        )
        self.assertEqual(child.parent_comment, parent)
        replies = parent.commentproduct_set.filter(parent_comment=parent)
        self.assertIn(child, replies)

    def test_commentproduct_cascade_delete(self):
        comment = CommentProduct.objects.create(user=self.user, product=self.product, text='Test')
        self.product.delete()
        self.assertFalse(CommentProduct.objects.filter(id=comment.id).exists())

    def test_commentuser_creation_and_str(self):
        c = CommentUser.objects.create(seller=self.other_user)
        self.assertEqual(c.seller, self.other_user)
        self.assertEqual(str(c), f"Comment on seller: {self.other_user.username}")
