from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.http import HttpResponse
from .models import Post,Comment
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm 
from django.core.mail import send_mail
from .forms import EmailPostForm,CommentForm



class PostListView(ListView):
    queryset=Post.objects.all()
    context_object_name='posts'
    paginate_by=3
    template_name='blogapp/post_list.html'

def post_list(request):
    object_list=Post.objects.all()
    paginator=Paginator(object_list,3) #3 Posts in a single page 
    page=request.GET.get('page')
    try:
        posts=paginator.page(page)
    except PageNotAnInteger:
        #If page is not an integer, then deliver the first page of results
        posts=paginator.page(1) 
        
    except EmptyPage:
        #if page is out of range, then deliver the last page of results 
        posts=paginator.page(paginator.num_pages)
    return render(request,'blogapp/post_list.html',{'posts':posts})

def post_detail(request,year,month,day,post):
    post=get_object_or_404(Post,slug=post,status='published',publish__year=year,publish__month=month,publish__day=day)
    #List of active comments for this post 
    comments=post.comments.filter(active=True)
    new_comment=None
    if request.method=='POST':
        #A comment was posted
        comment_form=CommentForm(data=request.POST)
        if comment_form.is_valid():
            #Create Comment Object but don't save to the database yet
            new_comment=comment_form.save(commit=False)
            #Assign the current post to the comment 
            new_comment.post=post
            #Save the comment to the datatabse 
            new_comment.save()
        else:
            comment_form=CommentForm()
        return render(request,'blogapp/post_detail.html',{'post':post,'comments':comments,
                                                          'new_comment':new_comment,
                                                          'comment_form':comment_form})
        
    
    
    return render(request,'blogapp/post_detail.html',{'post':post})

    

#Sharing our posts via email
def post_share(request,post_id):
    #Retrieve the post by id 
    post=get_object_or_404(Post,id=post_id)
    sent=False
    if request.method=='POST':
        #Formwas submitted 
        form=EmailPostForm(request.POST)
        if form.is_valid():
            #Form fields passed validation
            cd=form.cleaned_data
            post_url=request.build_absolute_uri(
                post.get_absolute_url()
            )
            subject=f"{cd['name']} recommends you read {post.title}"
            message=f"Read {post.title}at {post_url} \n\n"\
                f"{cd['name']} \'s comments : {cd['comments']}"
            send_mail(subject,message,'admin@myblog.com',[cd['to']])
            sent=True
            
    else:
        form=EmailPostForm()
    return render(request,'blogapp/post_share.html',{'form':form,'sent':sent})




















