from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name = 'home'),
    path('login/',views.signin,name='login'),
    path('register/',views.register,name='register'),
    path('updateprofile/',views.edit_profile,name='edit_profile'),
    path('business/',views.new_business,name='new_business'),
]