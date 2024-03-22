app_name='blogapp'
from django.urls import path
from . import views
from .feeds import LatestPostsFeed
from django.contrib.auth import views as auth_views


urlpatterns=[
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blogapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blogapp/home.html'), name='logout'),
    
    path('',views.home,name='home'),
    path('post_list',views.post_list,name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>',views.post_detail,name='post_detail'),
    path('<int:post_id>/share/',views.post_share,name='post_share'),
    #path('tag/<slug:tag_slug>/',views.post_list,name='post_list_by_tag'),
    
    path('feed/',LatestPostsFeed(),name='post_feed'),
    path('search/',views.post_search,name='post_search'),
    


    
    path('tag/<int:tag_id>/',views.related_posts,name='related_posts'),
    path('create_post',views.create_post,name='create_post'),
    path('edit_post/<int:pk>/',views.edit_post,name='edit_post'),
    path('delete_post/<int:pk>/',views.delete_post,name='delete_post'),
    
    path('user_posts/',views.my_posts,name='user_posts'),
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
]






















