from django import forms
from accounts.models import CustomUser
from .models import Course,InstructorProfile,StudentProgress,StudentProfile,AdministratorProfile 

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=['username','first_name','last_name','age','email']
class UserProfileForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=['username','first_name','last_name','age','email']
class StudentProfileForm(forms.ModelForm):
    class Meta:
        model=StudentProfile
        fields='__all__'
        
class InstructorProfileForm(forms.ModelForm):
    class Meta:
        model=InstructorProfile
        fields='__all__'
       
class AdministratorProfileForm(forms.ModelForm):
    class Meta:
        model=AdministratorProfile
        fields='__all__'
class StudentProgressForm(forms.ModelForm):
    class Meta:
        model=StudentProgress
        fields='__all__'
class CourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields='__all__'
         