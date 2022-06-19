from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import CreateAlertForm, CreateBusinessForm, CreateNeighbourhoodForm
from django.views.generic import CreateView


@login_required(login_url='/login/')
def index(request):
      return render(request,'index.html')



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


def search_results(request):

    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_businesses = Business.search_business(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"businesses": searched_businesses})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def create_neighbourhood(request):
    if request.method == 'POST':
        form = CreateNeighbourhoodForm(request.POST, request.FILES)
        if form.is_valid():
            neighbourhood = form.save(commit=False)
            neighbourhood.admin = request.user.profile.pk
            neighbourhood.save()
            return redirect('neighbourhoods')
    else:
        form = CreateNeighbourhoodForm()
    return render(request, 'neighbourhoods/create_neighbourhood.html', {'form':form})


def join_neighbourhood(request,pk):
    neighbourhood = get_object_or_404(Neighbourhood, id=pk)
    user = request.user
    user.profile.neighbourhood = neighbourhood
    user.profile.save()
    return redirect('neighbourhood_details', pk)

def change_neighbourhood(request, pk):
    neighbourhood = get_object_or_404(Neighbourhood, id=pk)
    user = request.user
    user.profile.neighbourhood = None
    user.profile.save()
    return redirect('neighbourhoods')

def neighbourhoods(request):
    neighbourhoods = Neighbourhood.objects.all()
    return render(request, 'neighbourhoods/neighbourhoods.html', {'neighbourhoods':neighbourhoods})

def neighbourhood_details(request,pk):
    neighbourhood = Neighbourhood.objects.filter(id=pk)
    businesses = Business.objects.filter(neighbourhood=pk)
    alerts = Alerts.objects.filter(neighbourhood=pk)
    if request.method == 'POST':
        form = CreateAlertForm(request.POST)
        
        if form.is_valid():
            alert = form.save(commit=False)
            alert.owner = request.user.profile
            alert.neighbourhood = request.user.profile.neighbourhood
            alert.save()
            return redirect('neighbourhood_details',pk)
    else:
        form = CreateAlertForm()
    context ={
      'neighbourhood':neighbourhood,
      'businesses': businesses,
      'alerts': alerts,
      'form': form,
    }
    return render(request, 'neighbourhoods/neighbourhood_details.html', context)
  
def create_business(request, pk):
    if request.method == 'POST':
        b_form = CreateBusinessForm(request.POST, request.FILES)
        if b_form.is_valid:
            business = b_form.save(commit=False)
            business.owner = request.user
            business.neighbourhood = request.user.profile.neighbourhood
            b_form.save()

            messages.success(request, f'Your business has been created successfully')
            return redirect('neighbourhood_details',pk)

    else:
        b_form = CreateBusinessForm(instance=request.user)
        

    context = {
      'b_form':b_form,
    }
    return render(request,'business/create_business.html', context)
