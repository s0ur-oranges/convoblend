from django.shortcuts import render,redirect
from .models import ChatRoom,ChatMessage
from django.contrib.auth.models import User
from .forms import RoomForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request , 'chat/home.html')

@login_required
def index(request):
    rooms=ChatRoom.objects.all()
    form=RoomForm()

    if request.method=='POST':
        form= RoomForm(request.POST)
        if form.is_valid():
            new_form=form.save(commit=False)
            new_form.user=request.user
            new_form.save()
        
        else:
            return render(request , 'chat/index.html', {'form':form})
        
        return redirect('/rooms/')
    
    room_name=request.GET.get('room_name')
    if room_name!="" and room_name is not None:
        rooms=ChatRoom.objects.filter(name__icontains=room_name)

    paginator=Paginator(rooms , 5)
    page=request.GET.get('page')
    rooms=paginator.get_page(page)

    return render(request , 'chat/index.html',{'rooms':rooms , 'form':form})


@login_required
def chatroom(request,slug):
    user=request.user
    room=ChatRoom.objects.get(slug=slug)
    slug=room.slug
    messages=ChatMessage.objects.filter(room=room)

    path=request.get_full_path() 
    path=request.build_absolute_uri(path) 

    return render(request , 'chat/chatroom.html' , {'room':room , 'messages':messages ,'user':user,'path':path})

@login_required
def edit_room(request , slug):
    room=ChatRoom.objects.get(slug=slug)
    form=RoomForm(request.POST or None , instance=room)

    if form.is_valid():
        form.save()
        return redirect('index')
    
    return render(request , 'chat/item_form.html' , {'form':form , 'room':room})

@login_required
def delete_room(request , slug):
    room=ChatRoom.objects.get(slug=slug)

    if request.method=='POST':
        room.delete()
        return redirect('index')

    return render(request , 'chat/delete_room.html' , {'room':room})  

