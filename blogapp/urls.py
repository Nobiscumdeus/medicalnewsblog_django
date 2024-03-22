app_name='blogapp'
from django.urls import path
from . import views
from .feeds import LatestPostsFeed
urlpatterns=[
    
    path('',views.post_list,name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>',views.post_detail,name='post_detail'),
    path('<int:post_id>/share/',views.post_share,name='post_share'),
    #path('tag/<slug:tag_slug>/',views.post_list,name='post_list_by_tag'),
    
    path('feed/',LatestPostsFeed(),name='post_feed'),
    path('search/',views.post_search,name='post_search'),
    


    
    path('tag/<int:tag_id>/',views.related_posts,name='related_posts'),
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
]






















