from ns_parcelbox_api.models import Humidity, Motion, Temperature
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TempSerializer
from .serializers import HumidSerializer
from .serializers import MotionSerializer

# api views

class TempViewSet(viewsets.ModelViewSet):
    queryset = Temperature.objects.all().order_by('date_created')
    serializer_class = TempSerializer

class HumidViewSet(viewsets.ModelViewSet):
    queryset = Humidity.objects.all().order_by('date_created')
    serializer_class = HumidSerializer

class MotionViewSet(viewsets.ModelViewSet):
    queryset = Motion.objects.all().order_by('date_created')
    serializer_class = MotionSerializer