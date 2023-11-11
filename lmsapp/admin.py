from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Course,StudentProfile,StudentProgress,InstructorProfile,AdministratorProfile
#Group models already registered 
admin.site.register(Course)
admin.site.register(StudentProfile)
admin.site.register(StudentProgress)
admin.site.register(InstructorProfile)
admin.site.register(AdministratorProfile)

# Register your models here.
