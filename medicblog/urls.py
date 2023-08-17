app_name='medicblog'
from django.urls import path
from . import views
#from django.views.generic import TemplateView 
from django.views.generic.base import TemplateView
urlpatterns=[
    path('',TemplateView.as_view(template_name='medicblog/home.html'),name='home'),
    #path('',views.TemplateView(template_name='medicblog/base.html')),
    path('post',views.MedicBlogListView.as_view(),name='list'),
    path('post/<int:pk>/',views.MedicBlogDetailView.as_view(),name='detail'),
    path('post/add/',views.MedicBlogCreateView.as_view(),name='create'),
    path('post/<int:pk>/edit',views.MedicBlogUpdateView.as_view(),name='update'),
    path('post/<int:pk>/delete',views.MedicBlogDeleteView.as_view(),name='delete'),
    
    path('email',views.EmailView.as_view(),name='email'),
    
    
    
    
    
    
]