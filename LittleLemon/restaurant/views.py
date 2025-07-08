from django.shortcuts import render
from rest_framework import viewsets
from .models import Menu, Reservation
from .serializers import MenuSerializer, ReservationSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.

def index(request):
    return render(request, 'index.html')

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]
