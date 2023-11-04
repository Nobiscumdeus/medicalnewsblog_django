from django.shortcuts import render
#from rest_framework.authentication import TokenAuthentication 
#from rest_framework.permissions import IsAuthenticated 



# Create your views here.
from rest_framework import viewsets
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset=Doctor.objects.all()
    serializer_class=DoctorSerializer
    #authentication_classes=[TokenAuthentication] #Here we set the authentication classses 
    #permission_classes=[IsAuthenticated]












