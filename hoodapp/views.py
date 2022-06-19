from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import *

from .forms import PostForm, ProfileUpdateForm


@login_required(login_url='/login/')
def home(request):
    hood = request.user.profile.neighbourhood

    title = f'Feed | {hood}'

    posts = Post.objects.filter(hood=hood)
    businesses = Business.objects.filter(hood=hood)
    amenities = Amenities.objects.filter(hood=hood)

    if request.method == 'POST':
      form = PostForm(request.POST)
      if form.is_valid():
         post = form.save(commit=False)
         post.author = request.user.profile
         post.hood = request.user.profile.neighbourhood
         post.save()
         return redirect('/')
    else:
      form = PostForm()

    context = {
      'title': title,
      'posts': posts,
      'businesses': businesses,
      'amenities': amenities,
      'form': form,
      'hood': hood
   }

    return render(request, 'index.html')

def signin(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have successfuly loged in")
            return redirect ('edit_profile')
    return render(request,'registration/login.html')

def register(request):
    if request.method == "POST":
        username=request.POST["username"]
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]

        if password1 !=password2:
            messages.error(request,'Password do not match')
            return render('/register')
        new_user=User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password1,
        ) 
        new_user.save() 
        return render (request,'registration/login.html')
    return render(request,'registration/register.html')


@login_required(login_url='register')
def edit_profile(request):

   title = 'Edit Profile'

   user = request.user

   if request.method == 'POST':
      form = ProfileUpdateForm(request.POST,request.FILES,instance=user.profile)
      if form.is_valid():
         form.save()
         return redirect('/')
   else:
      form = ProfileUpdateForm(instance=user.profile)

   context = {
      'title': title,
      'form': form
   }

   return render(request,'dash/edit_profile.html',context)