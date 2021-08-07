import rest_framework
from ns_parcelbox_api.models import Humidity, Motion, Temperature
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import TempSerializer
from .serializers import HumidSerializer
from .serializers import MotionSerializer

# api views

class TempViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Temperature.objects.all().order_by('date_created')
    serializer_class = TempSerializer

class HumidViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Humidity.objects.all().order_by('date_created')
    serializer_class = HumidSerializer

class MotionViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Motion.objects.all().order_by('date_created')
    serializer_class = MotionSerializer