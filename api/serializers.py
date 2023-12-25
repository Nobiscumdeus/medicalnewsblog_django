from rest_framework import serializers
from .models import Physician,Content



class PhysicianSerializer(serializers.ModelSerializer):
  
    class Meta:
        model=Physician
        fields='__all__'
        
        
        

    
class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Content
        fields='__all__'
        