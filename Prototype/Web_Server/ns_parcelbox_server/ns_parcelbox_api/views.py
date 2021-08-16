from ns_parcelbox_api.models import Humidity, Motion, Temperature
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import TempSerializer, HumidSerializer, MotionSerializer
from .models import Temperature, Humidity, Motion

# api view models

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


# index view
def index(request):
    """View function for main page"""

    # importing model data and creating objects here
    num_temperature = Temperature.objects.all().count()
    temperature_objs = Temperature.objects.order_by('date_created')
    temperature_latest = Temperature.objects.filter().order_by('-id')[:1]
    num_humidity = Humidity.objects.all().count()
    humidity_objs = Humidity.objects.order_by('date_created')
    humidity_latest = Humidity.objects.filter().order_by('-id')[:1]
    num_motion = Motion.objects.all().count()
    motion_objs = Motion.objects.order_by('date_created')
    motion_latest = Motion.objects.filter().order_by('-id')[:1]

    context = {
        'num_temperature': num_temperature,
        'temperature_objs': temperature_objs,
        'temperature_latest' : temperature_latest,
        'num_humdity': num_humidity,
        'humidity_objs': humidity_objs,
        'humidity_latest' : humidity_latest,
        'num_motion': num_motion,
        'motion_objs': motion_objs,
        'motion_latest' : motion_latest,
    }

    return render(request, 'index.html', context=context)