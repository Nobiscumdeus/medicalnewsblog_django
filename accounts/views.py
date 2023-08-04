from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from medicblog.models import Post
# Create your views here.

class SignupView(generic.CreateView):
    form_class=UserCreationForm
    success_url=reverse_lazy('login')
    template_name='registration/signup.html'
    
    """
    def CurrentUserProfile(request):
    user=request.user
    posts=Post.objects.filter(author=user)
    context={
        'user':user,
        'posts':posts
    }
    
    
    return render(request,'accounts/userprofile.html')
    """

    
    











