from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from restaurant.models import Menu
from rest_framework.authtoken.models import Token

class MenuViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass123')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        Menu.objects.create(name="Burger", description="Tasty Burger", price=5.99)

    def test_get_menu_list(self):
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_menu_item(self):
        data = {"name": "Pasta", "description": "Creamy pasta", "price": "9.99"}
        response = self.client.post('/menu/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
