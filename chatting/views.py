from django.shortcuts import render,redirect
from django.contrib.auth import login
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from .models import Room,Message
# Create your views here.

def frontpage(request):
    return render(request,'chatting/frontpage.html')

def signup(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        
        if form.is_valid():
            user=form.save()
            login(request,user)
            
            return redirect('chatting:login')
        else:
            form=SignUpForm()
        
    return render(request,'chatting/signup.html',{'form':form})


@login_required
def rooms(request):
    rooms=Room.objects.all()
    return render(request,'chatting/rooms.html',{'rooms':rooms})

@login_required
def room(request,slug):
    room=Room.objects.get(slug=slug)
    messages=Message.objects.filter(room=room)[0:25]
    
    return render(request,'chatting/room.html',{'room':room,'messages':messages})







