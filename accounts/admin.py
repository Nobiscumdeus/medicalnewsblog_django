
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.
#admin.site.register(CustomUser,CustomUserAdministrator)

@admin.register(CustomUser) 
class CustomUserAdministrator(admin.ModelAdmin):    
        add_form=CustomUserCreationForm
        form=CustomUserCreationForm
        model=CustomUser
        list_display=['email','username','sex','age','is_staff']
        fieldsets=UserAdmin.fieldsets +(
            (None,{'fields':('age','sex')}),
        
        )
    
'''        
class CustomUserAdmin(UserAdmin):
    add_form=CustomUserCreationForm
    form=CustomUserChangeForm
    model=CustomUser
    list_display=['email','username','age','is_staff']
    fieldsets=UserAdmin.fieldsets + (
        (None,{'fields':('age',)}),
    )     
'''    
        
     
    
        
     
    
        
     
    
        
     
    
        
     
    
        
     
    
        
     
    
        
     
    
        
     
    
        
     
    
        
     
    
        
     
    
        
     
    
        
     
    
        
     
    
        
     
    
        
     
    
        
     
    
        
     
    
        
    
    
        
    
    
    
    
    
    
        
    

    
    

