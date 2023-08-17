from django.contrib import admin
from .models import Post, Comments

# Register your models here.

class CommentsInline(admin.StackedInline):
    model=Comments

class PostAdmin(admin.ModelAdmin):
    '''
     list_display=('name','email','created','etc')
    list_filter=('active','created','updated')
    search_fields=('name','email')
    '''
   
    inlines=[
        CommentsInline,
    ]
admin.site.register(Post)
admin.site.register(Comments)



