import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Posts(models.Model):

 
    title =  models.CharField(max_length=50)
    category=  models.CharField(max_length=50)
    content =  models.TextField(blank=True, null=True)
    image =  models.CharField(max_length=100)
    date_published =  models.DateTimeField(auto_now_add=True)
    author =  models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    comments = models.IntegerField()
    likes =  models.IntegerField()



    def str(self):
        return self.id

