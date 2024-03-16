from django.db import models
from taggit.managers import TaggableManager
#from ckeditor.fields import RichTextField
from django_countries.fields import CountryField
from django.core.validators import MaxValueValidator,MinValueValidator




# Create your models here.
class Specialization(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}"
    

class Hospital(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name} @ {self.location}"
class InsuranceCompany(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}"



class MedicalSchool(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name} located in {self.location}"

        
#class Country(models.Model):
 #   name=models.CharField(max_length=100)
    
class Doctor(models.Model):
    GENDER_CHOICES=[
        ('M','Male'),
        ('F','Female'),
        ('O','Other'),
        ('N','Prefer not to say')
    ]
    AVAILABLE_CHOICES=[
        ('Y','Yes'),
        ('N','No')
    ]
    #Language Choices 
    LANGUAGE_CHOICES=[
        ('en','English'),('fr','French'),('es','Spanish'),
        ('de','German',),('it','Italian'),('pt','Portuguese'),
        ('nl','Dutch'),('ru','Russian'),('zh','Chinese'),
        ('ja','Japanese'),('ko','Korean'),('ar','Arabic'),('hi','Hindi'),('bn','Bengali'),('ur','Urdu'),
        ('tr','Turkish'),('sv','Swedish'),('da','Danish'),('no','Norwegian'),('fi','Finnish')
        
    ]
    first_name=models.CharField(max_length=100)
    middle_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    gender=models.CharField(
            max_length=2,
            choices=GENDER_CHOICES,
            default='N'
            )
    phone_number=models.CharField(max_length=15)
    
    email=models.EmailField()
    education=models.TextField()
    address=models.TextField()
    town=models.CharField(max_length=100,default="Prefer not to sat")
    state=models.CharField(max_length=100,default="Prefer not to say")
    skills=models.CharField(max_length=200,default="Coding")
    hobbies=models.CharField(max_length=200,default="Swimming")
    tags=TaggableManager()
   
    medical_school=models.ForeignKey(
        MedicalSchool,
        on_delete=models.CASCADE)
    #country=CountryField(blank=True)
    
    publications=models.TextField(help_text='Please provide the necessary details such as the title,year and author(s) of publication ')
    
    official_language=models.CharField(
            max_length=2,
            choices=LANGUAGE_CHOICES,default='en'
            )
    
    consultation_fee=models.DecimalField(
        max_digits=9,
        decimal_places=2)
    working_hours=models.TextField()
    bio=models.TextField()
    awards_and_recognitions=models.TextField()
    years_of_experience=models.PositiveIntegerField() 
    is_board_certified=models.BooleanField(default=False)
    license_number=models.CharField(
            max_length=20,
            null=True
            )
    average_rating=models.IntegerField(default=2,
                                       validators=[
                                           MaxValueValidator(5),
                                           MinValueValidator(1)
                                       ])
    available_for_consultation=models.CharField(
            max_length=2,
            null=True,blank=True,
            choices=AVAILABLE_CHOICES,
            default='Y'
            )
    website=models.URLField(
        max_length=200,
        null=True,
        blank=True
        )
    date_of_birth=models.DateField(
        null=True,
        blank=True)
    hospitals=models.ManyToManyField(Hospital,blank=True)
    insurance_companies=models.ManyToManyField(InsuranceCompany,blank=True)
    country=models.ForeignKey('cities_light.Country',on_delete=models.SET_NULL,null=True,blank=True)
    city=models.CharField(max_length=100,blank=True,null=True)
    
    created_at=models.DateTimeField(auto_now_add=True)
    last_updated=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Doctor {self.first_name} {self.last_name}"

