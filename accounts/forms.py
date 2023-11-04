from django import forms 
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,AuthenticationForm#These were only for the normal User model that comes with Django

from .models import CustomUser #We want a form for the CustomUSerModel we had created 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit,Field

#The Login form is extending the AuthenticationForm 
class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Username'})
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Password'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Email'})
    )
'''

   
class CustomUserLoginForm(AuthenticationForm):
    class Meta:
     
        fields=('username','email','password1')
        
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.fields['username'].widget.attrs.update(
            {'class':'form-control'},
            {'type':'text'},
            {'placeholder':'Enter your Password'}
        )
        self.fields['password1'].widegt.attrs.update(
            {'class':'form-control'},
            {'type':'password'},
            {'placeholder':'Enter your password'}
            
        )
        self.fields['email'].widget.attrs.update(
            {'class':'form-control'},
            {'type':'email'},
            {'placeholder':'You may or may not enter Email address'}
        )
'''

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=( 'username','email','age','sex','password1','password2')
        
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        #Apply Bootstrap classes , placeholders and other attributes 
        field_classes={
            'username':'form-control',
            'email':'form-control',
            'password1':'form-control',
            'password2':'form-control',
            'age':'form-control',
            'sex':'form-control'
        }
        field_placeholder={
            'username':'Please Enter your Names',
            'email':'Enter your Email address',
            'password1':'Enter your password',
            'password2':'Confirm your Password',
            'age':' How old are you in years ?',
            'sex':'Select your gender'
        }
        field_attributes={
            'username':{'type':'text','data-required':'true'},
            'email':{'type':'email'},
            'password1':{'type':'password','data-strength-meter':'true'},
            'password2':{'type':'password','data-strength-meter':'true'},
            
            
            
            #for birth 'birth':{'class':'datepicker','data-datepicker-options':'{"format":"dd/mm/yyyy"}'}
            
        }
        for field_name,css_class in field_classes.items():
            self.fields[field_name].widget.attrs['class']=css_class
            
        for field_name,placeholder_text in field_placeholder.items():
            self.fields[field_name].widget.attrs['placeholder']=placeholder_text
        
        for field_name,attributes in field_attributes.items():
            self.fields[field_name].widget.attrs.update(attributes)
        
       
'''
        
        field_attributes={
            'username':{'class':'custom-class','data-attribute':'value'},
            'passwor1':{'class':'another-class'},
            'sex':{'data-gender':'true'},
            'birth':{'class':'custom-class','data-datepicker':'true'},
        }
        for field_name,attributes in field_attributes.items():
            for attribute_name,attribute_value in attributes.items():
                self.fields[field_name].widget.attrs[attribute_name]=attribute_value
                
'''
        
     
       
                
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=CustomUser
        #fields=UserChangeForm.Meta.fields
        fields=('username','email','age','sex')


        
