from django.contrib import admin
from django import forms

# Register your models here.
from .models import Post,Comment,Tag
admin.site.site_header = 'Chasfat Applications'
admin.site.index_title = 'Chasfat Projects Admin'
admin.site.site_title = 'Chasfat Projects Admin'


class TagsInputField(forms.CharField):
    def clean(self,value):
        tag_names=[tag.strip() for tag in value.split(',')]
        tags=[]
        for tag_name in tag_names:
            tag,_=Tag.objects.get_or_create(name=tag_name)
            tags.append(tag)
        return tags 
    
'''
class TagInline(admin.TabularInline):
    model=Post.tags.through
    extra=1
'''  

class PostAdminForm(forms.ModelForm):
    tags=TagsInputField(required=False)
    
    class Meta:
        model=Post
        fields="__all__"
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    #inlines=[TagInline]
    form=PostAdminForm
    list_display=('title','slug','author','publish','status')
    list_filter=('status','created','publish','author')
    search_fields=('title','body')
    prepopulated_fields={'slug':('title',)}
    raw_id_fields=('author',)
    date_hierarchy=('publish')
    ordering=('status','publish')
    
admin.site.register(Tag)
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=('name','email','post','created','active')
    list_filter=('active','created','updated')
    search_fields=('name','email','body')