from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views import View #The View here is general, as opposed to say ListView which is specific
from django.core.exceptions import PermissionDenied



from django.core.mail import EmailMessage
from .forms import EmailForm  
class MedicBlogListView(ListView):  #LoginRequiredMixin can also be added here, It prevents users from doing activities like login etc until logged in
    model=Post
    template_name='medicblog/list.html'
    paginate_by=5
class MedicBlogDetailView(LoginRequiredMixin,DetailView):
    model=Post
    template_name='medicblog/detail.html'
    
class MedicBlogCreateView(LoginRequiredMixin,CreateView):
    model=Post
    template_name='medicblog/create.html'
    fields=['title','author','body']  #Just specifying the parts of the post we want created
    def form_valid(self, form): # new
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class MedicBlogUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView): #UserPassesTestMixin ensures only the right user can update or delete post
    model=Post
    template_name='medicblog/update.html'
    fields=['title','body']  #Note if you use fields=['__all__'] , all the fields are updated
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    def handle_no_permission(self):
        raise PermissionDenied("Ooops!!! You do not have access to this activity")
class MedicBlogDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    template="medicblog/delete.html"
    success_url=reverse_lazy('list') #Since after deletion, the detail doesn't exist anymore, just reverse to list page again then
    
      
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
class EmailView(View):
    template_name='medicblog/email.html'
    def get(self,request):
        form=EmailForm()
        return render(request,'medicblog/email.html',{'form':form})
    def post(self,request):
        form=EmailForm(request.POST)
        if form.is_valid():
            recipient=form.cleaned_data['recipient']
            subject=form.cleaned_data['subject']
            message=form.cleaned_data['message']
            
            email=EmailMessage(
                    subject=subject,
                    body=message,
                    from_email='emmanueladeola990@gmail.com',
                    to=[recipient],
            
                
            
            )
            try:
                email.send()
                success_message="Email sent successfully" 
            except Exception as e:
                success_message=f"An Error occurred: {str(e)}"
                #success_message="Ooops!!, An error occurred, could not be sent"
            return render(request,self.template_name,{'form':form,'success_message':success_message})
            
        else:
            return render(request,self.template_name,{'form':form})
        
        
        
