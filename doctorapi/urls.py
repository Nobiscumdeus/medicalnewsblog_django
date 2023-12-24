app_name='doctorapi'
from django.urls import path
from .views import SpecialtyViewSet,InsuranceCompanyViewSet,MedicalSchoolViewSet,DoctorViewSet, HospitalViewSet

urlpatterns=[
    
    path('specialty',SpecialtyViewSet.as_view({'get':'list','post':'create'}),name='doctor-list'),
    path('speciality/<int:pk>/',SpecialtyViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'}),name='doctor-detail'),    

    path('insurancecompany',InsuranceCompanyViewSet.as_view({'get':'list','post':'create'}),name='insurancecompany-list'),
    path('insurancecompany/<int:pk>/',InsuranceCompanyViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'}),name='insurancecompany-detail'),    

    path('medicalschool',MedicalSchoolViewSet.as_view({'get':'list','post':'create'}),name='medicalschool-list'),
    path('medicalschool/<int:pk>/',MedicalSchoolViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'}),name='medicalschool-detail'),    

  path('doctor',DoctorViewSet.as_view({'get':'list','post':'create'}),name='doctor-list'),
    path('doctor/<int:pk>/',DoctorViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'}),name='doctor-detail'),    
    
    
    
    path('hospital',HospitalViewSet.as_view({'get':'list','post':'create'}),name='hospital-list'),
    path('hospital/<int:pk>/',HospitalViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'}),name='hospital-detail'),    
]

