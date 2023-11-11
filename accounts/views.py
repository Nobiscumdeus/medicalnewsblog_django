from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views import View
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm,CustomLoginForm
from django.contrib.auth.decorators import login_required


from medicblog.models import Post

# Create your views here.

@login_required
def Home(request):
    return render(request,'accounts/home.html')

class SignUpView(View):
    template_name='accounts/signup.html'
    
    def get(self,request):
        form=CustomUserCreationForm
        return render(request,self.template_name,{'form':form})
    
    def post(self,request):
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user) #Automatically login the user after sign up
            return redirect('medicblog:list')
        return render(request,self.template_name,{'form':form})
    
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = CustomLoginForm












