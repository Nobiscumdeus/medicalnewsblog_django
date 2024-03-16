



from django import template
from blogapp.models import Post
from django.db.models import Count 


register=template.Library()
#Here we are adding filters to our django templates 
@register.filter
def capitalize_letter(value):
    return value.capitalize()