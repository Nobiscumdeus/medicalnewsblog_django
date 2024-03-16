from django import template
from blogapp.models import Post
from django.db.models import Count 




register=template.Library()
@register.simple_tag(name='total_posts')
def total_posts():
    return Post.published.count()


@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(total_comments=Count('comments').order_by('-total_comments')[:count])













#This reverses a string 
@register.simple_tag
def reverse_string(input_string):
    return input_string[::-1]






















#Here are Inclusion tags, which are simply templates displayed in other templates

@register.inclusion_tag('blogapp/recent_posts.html') #We are passing the template name to it 
def show_recent_posts(count=5):
    recent_posts=Post.published.order_by('-created')[:count]
    return {'recent_posts':recent_posts}








































