from django.test import TestCase
from restaurant.models import Menu, Reservation
from datetime import date, time

class MenuModelTest(TestCase):
    def test_menu_creation(self):
        item = Menu.objects.create(name="Pizza", description="Cheese Burst", price=12.50)
        self.assertEqual(str(item), "Pizza")

class ReservationModelTest(TestCase):
    def test_reservation_creation(self):
        reservation = Reservation.objects.create(
            name="John Doe",
            date=date.today(),
            time=time(19, 30),
            guests=4
        )
        self.assertEqual(str(reservation), f"John Doe - {reservation.date} at {reservation.time}")
