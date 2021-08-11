from rest_framework import serializers
from .models import Temperature, Humidity, Motion

class TempSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Temperature
        fields = ('id','temp','date_created')

class HumidSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Humidity
        fields = ('id','humidity_level','date_created')

class MotionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Motion
        fields = ('id','motion','date_created')