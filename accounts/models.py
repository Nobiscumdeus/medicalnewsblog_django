from django.db import models

from django.contrib.auth.models import AbstractUser #Helps us to modify the django built in models

# Create your models here.
class CustomUser(AbstractUser):
    SEX_CHOICES=[
       ( 'M','Male'),
        ('F','Female'),
    ]
    
    
    #Here we can add new or more fields to the user 
    age=models.PositiveIntegerField(null=True,blank=True)
    sex=models.CharField(null=True,blank=True,max_length=10,choices=SEX_CHOICES)
    
   
    
    

    
