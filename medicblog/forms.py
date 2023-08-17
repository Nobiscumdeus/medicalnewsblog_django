from django import forms 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit 
from .models import Post
class EmailForm(forms.Form):
    recipient=forms.EmailField()
    subject=forms.CharField()
    message=forms.CharField(required=False,widget=forms.Textarea)
    
    
class CommentForm(forms.Form):
    content=forms.CharField(widget=forms.Textarea)
    
    def __init__ (self,*args,**kwargs):
        super().__init__ (*args,**kwargs)
        self.helper=FormHelper()
        self.helper.form_method="post"
        self.helper.add_input(Submit('submit','Submit'))
        
class CreatePostForm(forms.Form):
    class Meta:
        model=Post
        fields=['title','author','body','tags']
        
    def __init__ (self,*args,**kwargs):
        super().__init__ (*args,**kwargs)
        self.helper=FormHelper()
        self.helper.form_method="post"
        self.add_input(Submit('submit','Submit'))


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','author','body','tags']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Changes'))

        

    
        
    
    
            