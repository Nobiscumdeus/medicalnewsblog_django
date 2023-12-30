from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import PhysicianViewSet,ContentViewSet,ObtainTokenView
from rest_framework.authtoken.views import obtain_auth_token
#from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView








router=DefaultRouter()
router.register(r'physicians',PhysicianViewSet,basename='physicians')
router.register(r'contents',ContentViewSet,basename='contents')



urlpatterns=[
    
    path('',include(router.urls)),
    path('api/token/', obtain_auth_token, name='api-token'),
  
    
    
]