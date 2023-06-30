from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CustomUser(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250, default='')
    name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)


    def __str__(self):
        return '%s' % (self.username)

class Vehicle(models.Model):

    choices = [
        ('Manual', "Manual"),
        ('Automatic',"Automatic"),
        ('Semi-automatic', "Semi-automatic")
    ]

    make = models.CharField(max_length=250)
    model = models.CharField(max_length=250)
    distance_travelled = models.CharField(max_length=250)
    first_registration = models.DateField()
    gearbox = models.CharField(max_length=250,choices=choices)
    number_of_owners = models.IntegerField()
    image = models.FileField(upload_to='images/')

    def __str__(self):
        return '%s-%s %s' % (self.make,self.model,self.first_registration)

class Post(models.Model):

    date_created = models.DateField(auto_now=True)
    vehicle = models.OneToOneField(
        Vehicle,
        on_delete=models.CASCADE,
        primary_key=True
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    note = models.TextField(null=True)

    def __str__(self):
        return '%s %s-%s' % (self.user.username,self.vehicle.make,self.vehicle.model)

class WishlistItem(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
