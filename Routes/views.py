from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.


@api_view(['GET'])
def points(request):
    if request.user.is_authenticated == False:
        return Response({"error": "Unathorized"})

    if request.method == 'GET':
        return Response({
            'list_of_points' : PointSerializer(Point.objects.all(), many=True).data
        })


@api_view(['GET'])
def routes(request):
    if request.user.is_authenticated == False:
        return Response({"error": "Unathorized"})

    if request.method == 'GET':
        return Response({
            'list_of_routes' : RouteSerializer(Route.objects.all(), many=True).data
        })