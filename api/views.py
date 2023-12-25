from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Physician,Content
from rest_framework import generics
from .serializers import PhysicianSerializer,ContentSerializer

#Third Party Imports
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

class PhysicianViewSet(viewsets.ModelViewSet):
    queryset=Physician.objects.all()
    serializer_class=PhysicianSerializer
    
class ContentViewSet(viewsets.ModelViewSet):
    queryset=Content.objects.all()
    serializer_class=ContentSerializer

def home(request):
    return HttpResponse('<h2> You are Welcome </h2>')

'''


class DoctorViewSet(viewsets.ModelViewSet):
    queryset=Doctor.objects.all()
    serializer_class=DoctorSerializer
    

'''


    


'''

class TestView(APIView):
    permission_classes=(IsAuthenticated,)
    def get(self,request,*args,**kwargs):
        data={
            'name':'Chasfat Projects',
            'age':23
        }
        return Response(data)
    def Content(self,request,*args,**kwargs):
        pass
        #serializer=ContentSerializer(data=request.data)
        
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
class DoctorList(generics.ListCreateAPIView):
    queryset=Doctor.objects.all()
    serializer_class=DoctorSerializer
    
class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Doctor.objects.all()
    serializer_class=DoctorSerializer
    
    

Create your views here.

def test_view(request):
    data={
    
   'name':'Chasfat Projects on the Codes ',
   'age':23
    }
    return JsonResponse(data,safe=False)
'''
