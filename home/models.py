from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Contact(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    message = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)


class Home(models.Model):
    subscribe = models.CharField(max_length=30)


class Base_Details(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    photo = models.ImageField(upload_to='self_image')



class Home_Slide_Images(models.Model):
    images = models.ImageField(upload_to='slide_images')