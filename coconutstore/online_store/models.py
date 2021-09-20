from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Brand(models.Model):
    Title = models.CharField(max_length=200)
    Description = models.TextField()
    Logo = models.ImageField(upload_to ='uploads/')
    Favicon = models.ImageField(upload_to ='uploads/')
    Color = models.CharField(max_length=200)

class Customer(models.Model):
    CITY_CHOICES = (('HYD','HYDERABAD'),('KMM',"KHAMMAM"))
    User = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    MobileNumber = PhoneNumberField(unique=True)
    FullName = models.CharField(max_length=200,blank=True,null=True)
    IsVerified = models.BooleanField(default=False)
    Otp = models.IntegerField(blank=True,null=True)

    def id_verified(self):
        return self.IsVerified


class DeliveryPartner(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    MobileNumber =  PhoneNumberField()
    FullName = models.CharField(max_length=200,null=True,blank=True)
    DOB = models.DateField(null=True,blank=True)
    ProfilePic = models.ImageField(upload_to ='uploads/',null=True,blank=True)
    IsVerified = models.BooleanField(default=False,null=True,blank=True)
    IsActive = models.BooleanField(default=False,null=True,blank=True)
    Otp = models.IntegerField(null=True,blank=True)

    def id_verified(self):
        return self.IsVerified
