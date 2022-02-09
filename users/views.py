from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.template import context
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm

from django.contrib.auth.decorators import login_required



def home(request):
  return render(request, 'users/home.html'  )


def register(request) :

  if request.method == 'POST':
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
       form.save()
       username = form.cleaned_data.get('username')
       raw_password = form.cleaned_data.get('password1')
       user = authenticate(username=username, password=raw_password)
       login(request, user)

       messages.success(request, f'Account created for {username}!')
       return redirect('login')


  else:
    form = UserRegistrationForm()

  
  return render(request, 'users/register.html' , { 'form' : form})

@login_required
def profile(request):
  if request.method == 'POST':
    u_form = UserUpdateForm(request.POST, instance=request.user)
    p_form = ProfileUpdateForm(request.POST,  request.FILES, instance=request.user.profile)

    if u_form.is_valid() and p_form.is_valid():
      u_form.save()
      p_form.save()
      messages.success(request, f'Your Account Has Been Updated!')
      return redirect('profile')

    
  else:
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)



  
  
  context = {
    'u_form': u_form,
    'p_form': p_form
  }
  return render(request, 'users/profile.html',context)