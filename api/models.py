from django.db import models
#Create the models here

class Doctor(models.Model):
    name=models.CharField(max_length=100)
    specialty=models.CharField(max_length=100)
    medical_school=models.CharField(max_length=100)
    county=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    positions=models.TextField(max_length=200)
    email=models.EmailField()
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    