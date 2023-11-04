app_name='doctorapi'
from django.urls import path
from .views import DoctorViewSet
urlpatterns=[
    
    path('doctors',DoctorViewSet.as_view({'get':'list','post':'create'}),name='doctor-list'),
    path('doctors/<int:pk>/',DoctorViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'}),name='doctor-detail'),    





]

