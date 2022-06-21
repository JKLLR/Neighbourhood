from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
# class Neighbourhood(models.Model):
#     name = models.CharField(max_length=30)
#     location = models.CharField(max_length=30)
#     logo = CloudinaryField('image')
#     health_dept = models.IntegerField(null=True, blank=True)
#     police_dept = models.IntegerField(null=True, blank=True)
#     admin = models.IntegerField("neighbourhood admin", blank=False, default=1)
#     description = models.TextField(max_length=200, blank=True)

#     def __str__(self):
#         return self.name

#     def create_neighbourhd(self):
#         self.save()

#     @classmethod
#     def delete_neighbourhd(cls, pk):
#         cls.objects.filter(pk=pk).delete()

#     @classmethod
#     def find_neighbourhd(cls, id):
#         search_results = cls.objects.filter(id=id)
#         return search_results

#     def update_neighbourhd(self, name):
#       self.name = name
#       self.save()

class Neighbourhood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=60)
    admin = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='hood')
    logo =CloudinaryField('images')
    description = models.TextField()
    health_dept = models.IntegerField(null=True, blank=True)
    police_dept = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.name} hood'

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=60, blank=True)
#     bio = models.TextField(max_length=200, blank=True)
#     profile_photo = CloudinaryField('image')
#     neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.SET_NULL, null=True,blank=True)
   

#     def __str__(self):
#         return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=80, blank=True)
    bio = models.TextField(max_length=254, blank=True)
    profile_photo = CloudinaryField('image')
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.SET_NULL, null=True, related_name='members', blank=True)

    def __str__(self):
        return f'{self.user.username} profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Business(models.Model):
    name = models.CharField(max_length=60)
    logo = CloudinaryField('image', blank=True)
    description = models.TextField(max_length=200, blank=True)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
      return self.name

    def create_busn(self):
        self.save()

    @classmethod
    def delete_busn(cls, pk):
        cls.objects.filter(pk=pk).delete()

    @classmethod
    def find_busn(cls, id):
        search_results = cls.objects.filter(id=id)
        return search_results

    def update_busn(self, name):
      self.name = name
      self.save()

    @classmethod
    def search_business(cls,search_term):
        businesses = cls.objects.filter(name__icontains=search_term)
        return businesses

# class Alerts(models.Model):
#     name = models.CharField(max_length=60)
#     content = models.TextField()
#     date_posted = models.DateTimeField(auto_now_add=True)
#     owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)

#     def __str__(self):
#       return self.name

class Alerts(models.Model):
    name = models.CharField(max_length=120)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='post_owner')
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='hood_post')