from django.contrib import admin
from .models import Post, Comments

# Register your models here.

class CommentsInline(admin.StackedInline):
    model=Comments

class PostAdmin(admin.ModelAdmin):
    inlines=[
        CommentsInline,
    ]
admin.site.register(Post)
admin.site.register(Comments)



