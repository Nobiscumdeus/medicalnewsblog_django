from django.contrib import admin
from .models import Doctor, Hospital,InsuranceCompany,MedicalSchool,Specialization
# Register your models here.

# Creating a customized admin for the  Doctor Model 
class DoctorAdmin(admin.ModelAdmin):
    list_display=['first_name','email','phone_number']
    search_fields=['first_name']
    
    fieldsets=[
        ('Personal Information',{'fields':['first_name','middle_name','last_name','bio']}),
        ('Contact Information',{'fields':['phone_number','address','email','town','state','website']}),
        ('Education Information',{'fields':['medical_school','awards_and_recognitions','skills']}),
        ('Professional Information',{'fields':['hospitals','working_hours','license_number','consultation_fee','available_for_consultation','is_board_certified','years_of_experience','average_rating']}),
        ('Financial Information',{'fields':['insurance_companies']}),
        ('Date Information',{'fields':['date_of_birth']}),
        ]
    


admin.site.register(Specialization)
admin.site.register(Hospital)
admin.site.register(InsuranceCompany)
admin.site.register(MedicalSchool)
admin.site.register(Doctor,DoctorAdmin)


