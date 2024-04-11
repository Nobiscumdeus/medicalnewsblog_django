"""
URL configuration for medicnewsblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

#To serve media files during development
from django.conf.urls.static import static
from django.conf import settings 
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
#In order to use sitemaps , we add the urls here from django
from django.contrib.sitemaps.views import sitemap
from blogapp.sitemaps import PostSitemap
sitemaps={
    
    'posts':PostSitemap,

    
}
'''
    Note, if you decide to use the auth_views here instead of the views of each app, django looks for the djanto templates in a registration folder,
    the main benefit of using the auth_views here may be to actually avoid repetition in all the apps
'''


urlpatterns = [
    path('admin/', admin.site.urls),
    path('medicblog/',include('medicblog.urls')),
    path('auth-api',include('rest_framework.urls')),
    path('api/',include('api.urls')),
    path('blogapp/',include('blogapp.urls')),
    #path('doctorschat/',include('chat.urls')),
    #Below are views that are used within the application 
    #path('login/',auth_views.LoginView.as_view(),name='login'),
    
    path('password_reset',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('password_reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password_reset_complete',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    
    
    
    
    #path('accounts/',include('django.contrib.auth.urls')), #doing this in oder to extend the Login,Logout,Signup pane provided by Django
    #path('accounts/login',auth_views.LoginView.as_view(),name='login'),
   # path('accounts/logout',auth_views.LogoutView.as_view(),name='logout'),
   
    #path('accounts/',include('django.contrib.auth.urls')),
   
    #path('accounts/',include('accounts.urls')),
    path('',include('pages.urls')),
    path('accounts/',include('accounts.urls')),
    
    path('doctorapi/',include('doctorapi.urls')),
    path('chatting/',include('chatting.urls')),
    
    #Adding our sitemap here 
    path('sitemap.xml',sitemap,{'sitemaps':sitemaps},
         name='django.contrib.sitemaps.views.sitemap')
 
    
    
    
    
    
    
    
]
#To serve media files in development 
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    
