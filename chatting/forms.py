from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 
from accounts.models import CustomUser


class SignUpForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=['username','password','password2']