from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# Create your models here.
class User(AbstractUser):
    is_admin=models.BooleanField('is admin',default=False)
    is_User=models.BooleanField('is user',default=False)
    is_sp=models.BooleanField('is servie_provider',default=False)

class Vendor(models.Model):
    vendorname=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=122,default=False)
    email=models.CharField(max_length=122)
    pas1=models.CharField(max_length=50)
    ph_no=models.CharField(max_length=50,null=True)
    services=models.CharField(max_length=122,default=False)
    image=models.ImageField(upload_to='images',blank=True,null=True)
    confirm=models.BooleanField(default=False)
    address=models.CharField(max_length=1000,null=True)
    desp=models.CharField(max_length=1000,null=True)
    def __str__(self):
        return self.email

class Coustmer(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=122,null=True)
    email=models.CharField(max_length=122)
    ph_no=models.CharField(max_length=50,null=True)
    pas1=models.CharField(max_length=50)
    address=models.CharField(max_length=300,null=True)
    image=models.ImageField(upload_to='user_images',blank=True,null=True)
    def __str__(self):
        return self.email

class Bookings(models.Model):
    user_email=models.ForeignKey(Coustmer,on_delete=models.CASCADE)
    Vendor_email=models.ForeignKey(Vendor,on_delete=models.CASCADE)
    user_ph=models.CharField(max_length=1000,null=True)
    user_add=models.CharField(max_length=1000,null=True)
    user_date=models.DateField()
    user_time= models.TimeField()
    user_name= models.CharField(max_length=1000,null=True)
    service_type=models.CharField(max_length=1000,null=True)
    status=models.CharField(max_length=1000,default="pending")
    vendor_name=models.CharField(max_length=1000,null=True)
    def __str__(self):
        return self.user_name
    
class Review(models.Model):
    user_email=models.CharField(max_length=1000,null=True)
    vendor_email=models.CharField(max_length=1000,null=True)
    star=models.CharField(max_length=1000,null=True)
    review=models.CharField(max_length=1000,null=True)
    def __str__(self):
        return self.vendor_email