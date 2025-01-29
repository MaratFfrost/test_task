from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import Sensor as s
from api.serializers import SensorSerializer



class Sensors(APIView):

  def get(self, request):

    try:
      sensors = s.objects.all()
      serializer = SensorSerializer(sensors, many=True)
      return Response(serializer.data)
    except Exception as e:

      return Response(
        {"error": str(e)},
        status=status.HTTP_400_BAD_REQUEST
      )
