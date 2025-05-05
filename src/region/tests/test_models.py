from django.test import TestCase
from region.models import Region

class RegionModelTest(TestCase):
    def setUp(self):
        # Ota hudud (parent) yaratamiz
        self.parent_region = Region.objects.create(name="Toshkent")

        # Shu ota hududga qarashli subregion yaratamiz
        self.sub_region = Region.objects.create(name="Yunusobod", parent_region=self.parent_region)

    def test_region_creation(self):
        """Region obyektlari to‘g‘ri yaratilganmi"""
        self.assertEqual(self.parent_region.name, "Toshkent")
        self.assertEqual(self.sub_region.name, "Yunusobod")

    def test_parent_region_relationship(self):
        """Subregionning parent_region to‘g‘ri belgilanganmi"""
        self.assertEqual(self.sub_region.parent_region, self.parent_region)

    def test_str_method(self):
        """__str__ metodi to‘g‘ri ismni qaytaradimi"""
        self.assertEqual(str(self.parent_region), "Toshkent")
        self.assertEqual(str(self.sub_region), "Yunusobod")

    def test_subregions_reverse_relation(self):
        """related_name='subregions' orqali parentdan subregionlar olinadimi"""
        subregions = self.parent_region.subregions.all()
        self.assertIn(self.sub_region, subregions)
