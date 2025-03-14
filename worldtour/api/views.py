from rest_framework.response import Response
from rest_framework.decorators import api_view
from asiatoursagency.models import Tour
from .serializers import TourSerializer

@api_view(['GET'])
def getData(request):
    items = Tour.objects.all()
    serializer = TourSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addData(request):
    serializer = TourSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)