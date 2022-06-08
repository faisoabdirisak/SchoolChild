from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name=models.CharField(max_length=200, blank=True, null=True)
    child_name=models.CharField(max_length=200, blank=True, null=True)
    child_age=models.IntegerField(blank=True, null=True)
    username=models.CharField(max_length=200, blank=True, null=True)
    location=models.CharField(max_length=200, blank=True, null=True)
    email=models.EmailField(max_length=500, blank=True, null=True)
    profile_image=models.ImageField(null=True, blank=True, upload_to='profiles/', default='profiles/math.jpg')
    child_image=models.ImageField(null=True, blank=True, upload_to='profiles/', default='profiles/math.jpg')
    created=models.DateField(auto_now_add=True)
    id=models.UUIDField(default=uuid4, unique=True, primary_key=True,editable=False)

    def __str__(self):
        return str(self.username)

