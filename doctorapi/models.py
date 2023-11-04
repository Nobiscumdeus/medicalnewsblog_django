from django.db import models
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from django_countries.fields import CountryField




# Create your models here.
class Specialization(models.Model):
    name=models.CharField(max_length=100)
class Hospital(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
class InsuranceCompany(models.Model):
    name=models.CharField(max_length=100)
class Publication(models.Model):
    title=models.CharField(max_length=200)
    publication_date=models.DateField()
class MedicalSchool(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
class Language(models.Model):
    LANGUAGE_CHOICES=[
        ('en','English'),('fr','French'),('es','Spanish'),
        ('de','German',),('it','Italian'),('pt','Portuguese'),
        ('nl','Dutch'),('ru','Russian'),('zh','Chinese'),
        ('ja','Japanese'),('ko','Korean'),('ar','Arabic'),('hi','Hindi'),('bn','Bengali'),('ur','Urdu'),
        ('tr','Turkish'),('sv','Swedish'),('da','Danish'),('no','Norwegian'),('fi','Finnish')
        
    ]
    name=models.CharField(max_length=50,choices=LANGUAGE_CHOICES)
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
    first_name=models.CharField(max_length=100)
    middle_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    gender=models.CharField(
            max_length=1,
            choices=GENDER_CHOICES
            )
    phone_number=models.CharField(max_length=15)
    
    email=models.EmailField()
    education=RichTextField()
    address=RichTextField()
    town=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    skills=models.CharField(max_length=200,default="Coding")
    hobbies=models.CharField(max_length=200,default="Swimming")
    tags=TaggableManager()
    specialization=models.ManyToManyField(
        Specialization)
    insurance_company=models.ManyToManyField(
        InsuranceCompany
         )
    medical_school=models.ForeignKey(
        MedicalSchool,
        on_delete=models.CASCADE)
    country=CountryField(blank=True)
    publications=models.ForeignKey(
        Publication,
        on_delete=models.CASCADE
        )
    languages_spoken=models.ManyToManyField(
        Language)
    hospital_affiliations=models.ManyToManyField(
        Hospital
        )
    consultation_fee=models.DecimalField(
        max_digits=9,
        decimal_places=2)
    working_hours=RichTextField()
    bio=RichTextField()
    awards_and_recognitions=RichTextField()
    years_of_experience=models.PositiveIntegerField() 
    is_board_certified=models.BooleanField(default=False)
    license_number=models.CharField(
            max_length=20,
            null=True
            )
    average_rating=models.DecimalField(
            max_digits=3,
            decimal_places=2,null=True,
            blank=True
            )
    #available_for_consultation=models.BooleanField(
     #   default=True
      #  )
    available_for_consultation=models.BooleanField(
          choices=AVAILABLE_CHOICES
      )
    website=models.URLField(
        max_length=200,
        null=True,
        blank=True
        )
    date_of_birth=models.DateField(
        null=True,
        blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    last_updated=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Doctor {self.first_name}{self.last_name}"

