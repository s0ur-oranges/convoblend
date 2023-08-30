from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile
from chat.models import ChatRoom
from django.contrib.auth.models import User
# Create your views here.

def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request , f'Congrats {username}! Your account is registered.')
            return redirect('create_profile')

    else: 
        form=RegisterForm()
    return render(request , 'users/register.html' , {'form':form})

@login_required
def profilepage(request , user_id):
    user=User.objects.get(id=user_id)
    profile=Profile.objects.get(user=user)
    rooms=ChatRoom.objects.filter(user=user)
    count=rooms.count()
    return render(request , 'users/profile.html', {'profile':profile , 'rooms':rooms , 'count':count})

@login_required
def create_profile(request):
    form=ProfileForm(request.POST or None)

    if form.is_valid():
        new_form=form.save(commit=False)
        new_form.user=request.user
        new_form.save()
        return redirect('index')
    return render(request , 'users/create_profile.html' , {'form':form})

@login_required
def update_profile(request , user_id):
    user=User.objects.get(id=user_id)
    profile=Profile.objects.get(user=user)
    form=ProfileForm(request.POST or None , instance=profile)

    if form.is_valid():
        form.save()
        return redirect('index')
    
    return render(request , 'users/create_profile.html' , {'form':form , 'user':user})

@login_required
def delete_account(request):
    user=request.user
    if request.method=='POST':
        user.delete()
        return redirect('index')

    return render(request , 'users/delete_account.html')  

    user.delete()
# Create your views here.
