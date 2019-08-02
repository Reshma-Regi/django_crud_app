from django.db import models

# Create your models here.

class sample(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    place = models.CharField(max_length=20)

class signin(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    place = models.CharField(max_length=20)
    password = models.CharField(max_length=10)
    email = models.EmailField(blank=True)

class log(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=10)

# models.py
class Hotel(models.Model):
	name = models.CharField(max_length=50)
	hotel_Main_Img = models.ImageField(upload_to='images/')
