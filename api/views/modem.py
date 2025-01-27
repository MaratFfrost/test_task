from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers

from api.models import Modem as m

class ModemSerializer(serializers.ModelSerializer):
  class Meta:
    model = m
    exclude = ["id"]

class Modems(APIView):

  def get(self, request):

    try:
      modems = m.objects.all()
      serializer = ModemSerializer(modems, many=True)
      return Response(serializer.data)

    except Exception as e:
      return Response(
        {"error": str(e)},
        status=status.HTTP_400_BAD_REQUEST
      )
