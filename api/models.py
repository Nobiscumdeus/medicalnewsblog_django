from django.db import models
#Create the models here

class Physician(models.Model):
    name=models.CharField(max_length=100)
    specialty=models.CharField(max_length=100)
    medical_school=models.CharField(max_length=100)
    county=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    positions=models.TextField(max_length=200)
    email=models.EmailField()
    
    def __str__(self):
        return self.name
    
class Content(models.Model):
    title=models.CharField(max_length=200)
    author=models.ForeignKey(Physician,on_delete=models.CASCADE)
    body=models.TextField(help_text="You can write your posts here",default="I am yet to write a post...")
    timestamp=models.DateTimeField(auto_now_add=True)
    
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.title} + {self.author}"
    