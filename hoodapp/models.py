from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Location(models.Model):
   
   name = models.CharField(max_length=50)

   def __str__(self):
      return self.name

class Profile(models.Model):

   user = models.OneToOneField(User, on_delete=models.CASCADE)
   avatar = CloudinaryField('image')

   def __str__(self):
      return self.user.username

class Neighbourhood(models.Model):
  
   name = models.CharField(max_length=50)
   location = models.ForeignKey(Location, on_delete=models.CASCADE)
   admin = models.ForeignKey(User, on_delete=models.CASCADE)

   def __str__(self):
      return self.name

   def create_neighbourhood(self):
      return self.save()

   def delete_neighbourhood(self):
      return self.delete()

   @classmethod
   def find_neighbourhood(cls,id):
      hood = cls.objects.filter(pk=id).first()
      return hood
   
   def update_neighbourhood(self):
      return self.save()

   @classmethod
   def update_occupants(cls,id):
      hood = cls.objects.filter(pk=id).first()
      occupants = hood.profile_set
      return occupants