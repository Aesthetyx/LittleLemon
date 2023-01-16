from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):     
    def testNewMenuItem(self):
        newMenuItem = Menu.objects.create(title="Test Menu Item", price=5, inventory=20)
        self.assertEqual(newMenuItem.__str__(), "Test Menu Item : 5")