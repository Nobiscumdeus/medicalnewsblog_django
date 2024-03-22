from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.http import HttpResponse
from .models import Post,Comment,Tag
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm,SearchForm
from django.core.mail import send_mail
from .forms import EmailPostForm,CommentForm


from django.db.models import Count
from django.contrib.postgres.search import SearchVector,SearchQuery,SearchRank

class PostListView(ListView):
    queryset=Post.objects.all()
    context_object_name='posts'
    paginate_by=3
    template_name='blogapp/post_list.html'

def post_list(request):
    object_list=Post.published.all()
    
        
    paginator=Paginator(object_list,4) #3 Posts in a single page 
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
            #List of similar posts
            post_tags_ids=post.tags.values_list('id',flat=True)
            #similar_posts=Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
            #similar_posts=similar_posts.annotate(same_tags=Count('tags')).order_by('-same-tags','-publish')[:4]
            
        else:
            comment_form=CommentForm()
        return render(request,'blogapp/post_detail.html',{'post':post,
                                                          'comments':comments,
                                                          'new_comment':new_comment,
                                                          'comment_form':comment_form,
                                                          #'similar_posts':similar_posts
                                                          })
        
    
    
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

def post_search(request):
    form=SearchForm()
    query=None
    results=[]
    if 'query' in request.GET:
        form=SearchForm(request.GET)    
        if form.is_valid():
            query=form.cleaned_data['query']
            '''
             results=Post.published.annotate(
                search=SearchVector('title','body'),
                ).filter(search=query)
            '''
            #search_vector=SearchVector('title','body')#
            #Applying weights to our search
            search_vector=SearchVector('title',weight='A') + SearchVector('body',weight='B')
            search_query=SearchQuery(query)
            results=Post.published.annotate(
                search=search_vector,
                rank=SearchRank(search_vector,search_query)
                
            ).filter(rank__gte=0.3).order_by('-rank')
            #Initially filter(search=search_query).order_by('-rank)
            
           
           
    return render(request,'blogapp/post_search.html',
            { 'form':form,
                'query':query,
                'results':results}
    )
    
    
    
    
    



def related_posts(request, tag_id):
    tag_name = get_object_or_404(Tag, id=tag_id)
    related_posts = tag_name.posts.all()
    return render(request, 'blogapp/related_posts.html', {'tag_name': tag_name, 'related_posts': related_posts})














