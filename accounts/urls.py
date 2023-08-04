from . import views; 
from django.urls import path 

 
urlpatterns=[
    
    path('signup',views.SignupView.as_view(),name='signup'),
    #path('userprofile',views.CurrentUserProfile,name='userprofile')
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    ]