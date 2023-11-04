from django.shortcuts import render
from rest_framework import viewsets
from .serializers import GDSSerializer
from .models import GDS

# Create your views here.
class GDSViewSet(viewsets.ModelViewSet):
    serializer_class = GDSSerializer
    queryset = GDS.objects.all().order_by('created_at')
    
