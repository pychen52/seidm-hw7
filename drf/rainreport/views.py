# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from rainreport.models import Rainfall, Station
from rainreport.serializers import RainfallSerializer, StationSerializer
from rest_framework import generics

class RainfallList(generics.ListAPIView):
    queryset = Rainfall.objects.all()
    serializer_class = RainfallSerializer

class RainfallDetail(generics.RetrieveAPIView):
    queryset = Rainfall.objects.all()
    serializer_class = RainfallSerializer

class StationList(generics.ListAPIView):
    serializer_class = StationSerializer
    
    def get_queryset(self):
        queryset = Station.objects.all()
        county = self.request.query_params.get('county', None)
        if county is not None:
            queryset = queryset.filter(county=county)
        return queryset
