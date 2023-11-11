from django.shortcuts import render,redirect
from django.http import HttpResponse 
from accounts.models import CustomUser
from .models import Course,InstructorProfile,StudentProgress,StudentProfile,AdministratorProfile 
from django.views.generic.edit import CreateView,UpdateView
from .forms import UserRegistrationForm,UserProfileForm,StudentProfileForm,InstructorProfileForm,AdministratorProfileForm



from django.contrib.auth.decorators import login_required 

# Create your views here.
@login_required
def home(request):
    return render(request,'lmsapp/home.html')
@login_required
def dashboard(request):
    return render(request,'lmsapp/dashboard.html')

























