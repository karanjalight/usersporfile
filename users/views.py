from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .forms import UserRegistrationForm



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


def profile(request):
  return render(request, 'users/profile.html')