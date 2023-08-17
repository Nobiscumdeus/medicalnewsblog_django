from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views import View
from django.contrib.auth import login
from .forms import CustomUserCreationForm


from medicblog.models import Post
# Create your views here.





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
    
    











