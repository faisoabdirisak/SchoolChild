from uuid import uuid4
from django.db import models

# Create your models here.
class Sliders(models.Model):
   title=models.CharField(max_length=200)
   sub_title=models.CharField(max_length=500,null=True, blank=True)
   one_image=models.ImageField(null=True, blank=True, default='math.jpg')


   def __str__(self):
        return self.title


  

class Activities(models.Model):
     title=models.CharField(max_length=200)
     sub_title=models.CharField(max_length=200,null=True, blank=True)
     line_one=models.CharField(max_length=200,null=True, blank=True)
     line_two=models.CharField(max_length=200,null=True, blank=True)
     line_three=models.CharField(max_length=200,null=True, blank=True)
     line_four=models.CharField(max_length=200,null=True, blank=True)
     line_five=models.CharField(max_length=200,null=True, blank=True)
     line_six=models.CharField(max_length=200,null=True, blank=True)
     featured_image=models.ImageField(null=True, blank=True, default='math.jpg')
     created=models.DateField(auto_now_add=True)
     id=models.UUIDField(default=uuid4, unique=True, primary_key=True,editable=False)


     def __str__(self):
        return self.title

class About(models.Model):
   title=models.CharField(max_length=200)
   sub_title=models.CharField(max_length=200,null=True, blank=True)
   another_title=models.CharField(max_length=200,null=True, blank=True)  
   about_image=models.ImageField(null=True, blank=True, default='math.jpg') 
   description=models.TextField()
   created=models.DateField(auto_now_add=True)
   id=models.UUIDField(default=uuid4, unique=True, primary_key=True,editable=False)   


   def __str__(self):
        return self.title

class Contact(models.Model):
   contact_image=models.ImageField(null=True, blank=True, default='math.jpg') 
   created=models.DateField(auto_now_add=True)
   id=models.UUIDField(default=uuid4, unique=True, primary_key=True,editable=False)   


         