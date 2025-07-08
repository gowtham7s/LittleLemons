from django.urls import path
from . import views

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuViewSet, ReservationViewSet

router = DefaultRouter()
router.register(r'menu', MenuViewSet)
router.register(r'reservation', ReservationViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('', include(router.urls)),
]
