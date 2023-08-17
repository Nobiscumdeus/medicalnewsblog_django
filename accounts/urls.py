from . import views; 
from django.urls import path 
from django.contrib.auth import views as auth_views
app_name='accounts'

 
urlpatterns=[
    
    path('signup/',views.SignUpView.as_view(),name='signup'),
    #path('userprofile',views.CurrentUserProfile,name='userprofile')
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    ]