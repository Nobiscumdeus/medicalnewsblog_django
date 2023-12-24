from rest_framework import serializers
from .models import Specialization,Doctor,Hospital,InsuranceCompany,MedicalSchool


class SpecializationSerializer(serializers.ModelSerializer):
   
    class Meta:
        model=Specialization
        fields='__all__'
        
       
class HospitalSerializer(serializers.ModelSerializer):
   
    class Meta:
        model=Hospital
        fields='__all__' 
        
class InsuranceCompanySerializer(serializers.ModelSerializer):
   
    class Meta:
        model=InsuranceCompany
        fields='__all__' 

class MedicalSchoolSerializer(serializers.ModelSerializer):
   
    class Meta:
        model=MedicalSchool
        fields='__all__' 
class DoctorSerializer(serializers.ModelSerializer):
   
    class Meta:
        model=Doctor
        fields='__all__' 


        
        
        