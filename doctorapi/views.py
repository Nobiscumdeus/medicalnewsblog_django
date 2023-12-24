from django.shortcuts import render
#from rest_framework.authentication import TokenAuthentication 
#from rest_framework.permissions import IsAuthenticated 



# Create your views here.
from rest_framework import viewsets
from .models import Specialization,InsuranceCompany,MedicalSchool,Hospital,Doctor
from .serializers import SpecializationSerializer,MedicalSchoolSerializer,DoctorSerializer,HospitalSerializer,InsuranceCompanySerializer

class SpecialtyViewSet(viewsets.ModelViewSet):
    queryset=Specialization.objects.all()
    serializer_class=SpecializationSerializer
    #authentication_classes=[TokenAuthentication] #Here we set the authentication classses 
    #permission_classes=[IsAuthenticated]


class InsuranceCompanyViewSet(viewsets.ModelViewSet):
    queryset=InsuranceCompany.objects.all()
    serializer_class=InsuranceCompanySerializer
    
class HospitalViewSet(viewsets.ModelViewSet):
    queryset=Hospital.objects.all()
    serializer_class=HospitalSerializer
    
class MedicalSchoolViewSet(viewsets.ModelViewSet):
    queryset=MedicalSchool.objects.all()
    serializer_class=MedicalSchoolSerializer
    
class DoctorViewSet(viewsets.ModelViewSet):
    queryset=Doctor.objects.all()
    serializer_class=DoctorSerializer
    
    








