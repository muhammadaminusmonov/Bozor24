# your_app/tests/test_models.py

from django.test import TestCase
from category.models import Category

class CategoryModelTest(TestCase):

    def test_create_category_without_parent(self):
        category = Category.objects.create(name="Electronics")
        self.assertEqual(category.name, "Electronics")
        self.assertIsNone(category.parent_category)
        self.assertIsNotNone(category.add_category_at)

    def test_create_category_with_parent(self):
        parent = Category.objects.create(name="Electronics")
        child = Category.objects.create(name="Phones", parent_category=parent)
        self.assertEqual(child.parent_category, parent)
        self.assertIn(child, parent.subcategories.all())
