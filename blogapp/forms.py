from django import forms 
from .models import Comment,Post,Tag
from django.forms.models import inlineformset_factory


#TagFormSet = inlineformset_factory(Post, Tag, fields=['name'], extra=1)


class EmailPostForm(forms.Form):
    name=forms.CharField(max_length=25)
    email=forms.EmailField()
    to=forms.EmailField()
    comments=forms.CharField(required=False,
                             widget=forms.Textarea)
    
    

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment    
        fields=('name','email','body')
        
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        #Adding Bootstrap classes to form fields
        self.fields['name'].widget.attrs.update({'class':'form-select','placeholder':'What are your names'})
        self.fields['email'].widget.attrs.update({'class':'form-select','placeholder':'Your email address'})
        self.fields['body'].widget.attrs.update({'class':'form-select','row':'9','col':'15','placeholder':'Enter your comments '})

       
    
    
        
        
    
    
class SearchForm(forms.Form):
    query=forms.CharField()
    
    
    
    
    
    