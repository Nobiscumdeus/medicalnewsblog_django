from rest_framework import serializers
from .models import Doctor,Post

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields='__all__'
        
        
        

    
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=[
            'title',
            'description'
        ]