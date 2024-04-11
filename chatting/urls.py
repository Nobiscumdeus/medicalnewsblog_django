app_name='chatting'
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views #takes care of logout action 



urlpatterns=[
    path('front_page',views.frontpage,name='front_page'),
    path('signup',views.signup,name='signup'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('login',auth_views.LoginView.as_view(template_name='chatting/login.html'),name='login'),
    path('rooms',views.rooms,name='rooms'),
    path('<slug:slug>/',views.room,name='room'),
    
    
    
    
    ]
