from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(cls):
        # set up test data
        cls.testMenuItemOne = Menu.objects.create(title="Test Menu Item 1", price=10, inventory=20)
        cls.testMenuItemTwo = Menu.objects.create(title="Test Menu Item 2", price=5, inventory=50)
        cls.testMenuItemThree = Menu.objects.create(title="Test Menu Item 3", price=7, inventory=8)
        # set up user
        user = User.objects.create_superuser("admin", "admin@littlelemon.com", "admin")
        user.save()
        
    def test_get_all(self):
        client = Client()
        client.login(username="admin", password="admin")
        viewResponse = client.get(reverse("menu"))
        expectedResponse = Menu.objects.all()
        serializedExpectedResponse = MenuSerializer(expectedResponse, many=True)
        self.assertEqual(viewResponse.data, serializedExpectedResponse.data)
        