from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
from django.utils import timezone

#To utilize taggit models 
#from taggit.managers import TaggableManager



# Create your models here.


class Post(models.Model):
    title=models.CharField(max_length=200)
    #author=models.ForeignKey(User,on_delete=models.CASCADE)
    #We are using a custom user now instead of the default auth user 
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    body=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True) 
    #tags=TaggableManager(related_name='medicblog') #This is comming from the taggit library installed
    

    
    def __str__ (self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('medicblog:detail',args=[str(self.id)])   
    
        
class Comments(models.Model): # new
    article = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    comment = models.CharField(max_length=140)
    body=models.TextField(default="Expect new comments soon...")
    author = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,related_name='comments'
    )
    def __str__(self):
        return self.comment
        
    def get_absolute_url(self):
        return reverse('medicblog:list')
            
    
   
      
    

    
