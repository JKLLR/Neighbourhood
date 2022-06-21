from django import forms
from .models import Alerts, Business, Neighbourhood, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#update profile email and username
class CreateNeighbourhoodForm(forms.ModelForm):

    class Meta:
        model = Neighbourhood
        exclude = ['admin',]

class CreateAlertForm(forms.ModelForm):

    class Meta:
        model = Alerts
        fields = ['owner', 'content']

class CreateBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['owner', 'neighbourhood']

class BusinessUpdateForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['owner', 'neighbourhood']


# class UserUpdateForm(forms.ModelForm):
   
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'neighbourhood')