from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Physician,Content
from rest_framework import generics,permissions,status
from .serializers import PhysicianSerializer,ContentSerializer,TokenObtainSerializer

#Third Party Imports
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication 
from rest_framework.authtoken.models import Token



from rest_framework import viewsets

class PhysicianViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classses=[IsAuthenticated]
    queryset=Physician.objects.all()
    serializer_class=PhysicianSerializer
    
class ContentViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classses=[IsAuthenticated]
    queryset=Content.objects.all()
    serializer_class=ContentSerializer
    
class ObtainTokenView(APIView):
    authentication_classes=[]
    def post(self,request,*args,**kwargs):
        
        serializer=TokenObtainSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['username']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key},status=status.HTTP_200_OK)

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
