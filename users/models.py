from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user =models.ForeignKey(User , on_delete=models.CASCADE)
    image=models.ImageField(default='images/profile_pictures/profilepic.jpg' , upload_to='images/profile_pictures')
    location=models.CharField(max_length=100)
    interests=models.TextField(max_length=2000)
    bio=models.TextField(max_length=2000 , default="I hope to connect with more people with similar interests",blank=True)
    private=models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username