from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Location(models.Model):
   
   name = models.CharField(max_length=50)

   def __str__(self):
      return self.name


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

class Profile(models.Model):
    
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   avatar = CloudinaryField('image')
   neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, null=True)

   def __str__(self):
      return self.user.username

class Category(models.Model):
   
   name = models.CharField(max_length=50)

   def __str__(self):
      return self.name



class Business(models.Model):

   name = models.CharField(max_length=50)
   email = models.EmailField(max_length=254)
   tel = models.IntegerField()
   hood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
   category = models.ForeignKey(Category, on_delete=models.CASCADE)
   owner = models.ForeignKey(Profile,on_delete=models.CASCADE)

   def __str__(self):
      return self.name


class Post(models.Model):
   
   content = models.CharField(max_length=280)
   author = models.ForeignKey(Profile, on_delete=models.CASCADE)
   hood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
   category = models.CharField(max_length=50,default='General')

   def __str__(self):
      return self.content
   
class Amenities(models.Model):
  
   name = models.CharField(max_length=50)
   tel = models.IntegerField()
   email = models.EmailField(max_length=254)
   amenity_type = models.CharField(max_length=50)
   hood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)

   def __str__(self):
      return self.name


class Comment(models.Model):
   
   comment = models.CharField(max_length=50)
   comment_on = models.ForeignKey(Post, on_delete=models.CASCADE)
   comment_by = models.ForeignKey(Profile, on_delete=models.CASCADE)

   def __str__(self):
      return self.comment