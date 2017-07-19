from rest_framework import serializers
from rainreport.models import Rainfall, Station

class RainfallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rainfall
        fields = '__all__' 

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__' 
