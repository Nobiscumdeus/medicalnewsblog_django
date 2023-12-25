from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import PhysicianViewSet,ContentViewSet
router=DefaultRouter()
router.register(r'physicians',PhysicianViewSet)
router.register(r'contents',ContentViewSet)

urlpatterns=[
    
    path('',include(router.urls)),
    
    
]