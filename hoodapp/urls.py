from django.urls import path
from . import views

urlpatterns=[
    path('home/',views.home,name = 'home'),
    path('',views.signin,name='login'),
    path('register/',views.register,name='register'),
]