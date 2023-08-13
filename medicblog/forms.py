from django import forms 
class EmailPostForm(forms.Form):
    recipient=forms.EmailField()
    subject=forms.CharField()
    message=froms.CharField(required=False,widget=forms.Textarea)
    
        
    
    
            