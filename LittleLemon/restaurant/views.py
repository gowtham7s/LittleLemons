from django.shortcuts import render
from rest_framework import viewsets
from .models import Menu, Reservation
from .serializers import MenuSerializer, ReservationSerializer

# Create your views here.

def index(request):
    return render(request, 'index.html')

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
