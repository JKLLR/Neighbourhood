from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name = 'home'),
    path('login/',views.signin,name='login'),
    path('register/',views.register,name='register'),
    path('updateprofile/',views.edit_profile,name='edit_profile'),
    path('newhood/',views.new_hood,name='new_hood'),
    path('business/',views.new_business,name='new_business'),
    path('amenity/',views.new_amenity,name='new_amenity'),
]