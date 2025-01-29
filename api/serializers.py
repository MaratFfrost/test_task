from rest_framework import serializers

from api.models import Modem as m
from api.models import Counter as c
from api.models import Sensor as s

class SensorSerializer(serializers.ModelSerializer):
  class Meta:
    model = s
    exclude = ["id"]

class ModemSerializer(serializers.ModelSerializer):
  class Meta:
    model = m
    exclude = ["id"]

class CounterSerializers(serializers.ModelSerializer):
  class Meta:
    model = c
    exclude = ["id"]
