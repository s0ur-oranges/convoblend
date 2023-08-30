from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.fields import AutoSlugField
from django.core.validators import MaxValueValidator

class MyValidator(MaxValueValidator):
    message = 'Your question is too long.'

# Create your models here.

class ChatRoom(models.Model):
    def __str__(self):
        return self.name
    
    name=models.CharField(max_length=300)
    user=models.ForeignKey(User , on_delete=models.CASCADE)
    about=models.TextField(max_length=500 , default=f"Lets talk!")
    slug=AutoSlugField(('slug'), max_length=50, unique=True, populate_from=('name',))

class ChatMessage(models.Model):
     user=models.ForeignKey(User , on_delete=models.CASCADE)
     room=models.ForeignKey(ChatRoom , on_delete=models.CASCADE)
     message_content=models.TextField()
     date=models.DateTimeField(auto_now=True)

     class Meta:
         ordering=('date',)