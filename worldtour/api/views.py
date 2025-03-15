from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from asiatoursagency.models import Tour
from .serializers import TourSerializer
from django.http import JsonResponse

@api_view(['GET'])
def getData(request,id=None):
    if id:
        items = Tour.objects.get(id=id)
        serializer = TourSerializer(items)
    else:
        items = Tour.objects.all()
        serializer = TourSerializer(items, many=True)
        
    return JsonResponse({'Tours':serializer.data},status=status.HTTP_200_OK)
    


@api_view(['POST'])
def addData(request):
    serializer = TourSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)