from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

# Create your views here.

class MedicBlogListView(ListView):  #LoginRequiredMixin can also be added here, It prevents users from doing activities like login etc until logged in
    model=Post
    template_name='medicblog/list.html'
    
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
    
class MedicBlogUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    template_name='medicblog/update.html'
    fields=['title','body']  #Note if you use fields=['__all__'] , all the fields are updated
    
class MedicBlogDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    template="medicblog/delete.html"
    success_url=reverse_lazy('list') #Since after deletion, the detail doesn't exist anymore, just reverse to list page again then
    
    
    
    





