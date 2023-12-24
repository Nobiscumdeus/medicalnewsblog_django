from django.contrib import admin
from .models import Doctor, Hospital,InsuranceCompany,MedicalSchool,Specialization
# Register your models here.



admin.site.register(Specialization)
admin.site.register(Hospital)
admin.site.register(InsuranceCompany)
admin.site.register(MedicalSchool)
admin.site.register(Doctor)


