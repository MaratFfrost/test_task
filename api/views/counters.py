from rest_framework import  status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Counter as c
from api.serializers import CounterSerializers



class Counters(APIView):

  def get(self, request):

    try:
      sensors = c.objects.all()
      serializer = CounterSerializers(sensors, many=True)
      return Response(serializer.data)

    except Exception as e:
      return Response(
        {"error": str(e)},
        status=status.HTTP_400_BAD_REQUEST
      )
