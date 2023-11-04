from django.contrib import admin
from .models import Doctor,Hospital,InsuranceCompany,Publication,MedicalSchool,Language,Specialization
# Register your models here.
admin.site.register(Doctor)
admin.site.register(Specialization)
admin.site.register(Hospital)
admin.site.register(InsuranceCompany)
admin.site.register(Publication)
admin.site.register(MedicalSchool)
admin.site.register(Language)
