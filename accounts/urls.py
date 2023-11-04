app_name="accounts"
from . import views
from django.urls import path 
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView




 
urlpatterns=[
    path('home/',views.Home,name='home'),
    path('signup/',views.SignUpView.as_view(),name='signup'),
    path('login/',views.CustomLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='accounts:signup'),name='logout'),
    #path('userprofile',views.CurrentUserProfile,name='userprofile')
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    ]