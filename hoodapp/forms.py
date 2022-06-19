from django import forms

from .models import Business, Neighbourhood, Post, Profile

class ProfileUpdateForm(forms.ModelForm):
    
   class Meta:
      model = Profile
      fields = ['avatar','neighbourhood']


class NeighbourhoodForm(forms.ModelForm):

   class Meta:
      model = Neighbourhood
      fields = ['name','location']

class BusinessForm(forms.ModelForm):

   class Meta:
      model = Business
      fields = ['name','category','email','tel']

class PostForm(forms.ModelForm):
 
   CATEGORIES = (
      ('', 'Select a Category'),
      ('Alert','Alert'),
      ('General','General'),
      ('Announcement','Announcement'),
   )

   content =  forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'What\'s new?'}))
   category = forms.ChoiceField(choices=CATEGORIES,widget=forms.Select())

   class Meta:
      model = Post
      fields = ['content','category']