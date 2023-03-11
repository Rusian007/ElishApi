from rest_framework import serializers
from .models import *
class PointSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    latitude = serializers.DecimalField(max_digits=9, decimal_places=6)
    longitude = serializers.DecimalField(max_digits=9, decimal_places=6)


class RouteSerializer(serializers.ModelSerializer):
    starting_point_name = serializers.CharField(source='starting_point.name')
    ending_point_name = serializers.CharField(source='ending_point.name')
    class Meta:
        model = Route
        fields = '__all__'