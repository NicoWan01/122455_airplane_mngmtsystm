django-admin startproject airline_booking
cd airline_booking
django-admin startapp bookings
from django.db import models

class Flight(models.Model):
    flight_number = models.CharField(max_length=10, unique=True)
    departure = models.DateTimeField()
    arrival = models.DateTimeField()
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return self.flight_number

class Passenger(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    flight = models.ForeignKey(Flight, related_name='passengers', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
from rest_framework import serializers
from .models import Flight, Passenger

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

class PassengerSerializer(serializers.ModelSerializer):
    flight = FlightSerializer()

    class Meta:
        model = Passenger
        fields = '__all__'
from rest_framework import viewsets
from .models import Flight, Passenger
from .serializers import FlightSerializer, PassengerSerializer

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from bookings.views import FlightViewSet, PassengerViewSet

router = DefaultRouter()
router.register(r'flights', FlightViewSet)
router.register(r'passengers', PassengerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
pip install django-filter
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Flight, Passenger
from .serializers import FlightSerializer, PassengerSerializer

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['origin', 'destination']
    search_fields = ['flight_number']
    ordering_fields = ['departure', 'arrival']

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['flight']
    search_fields = ['first_name', 'last_name', 'email']
    ordering_fields = ['first_name', 'last_name']
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}
