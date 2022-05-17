import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Posts(models.Model):
    id = models.IntegerField(primary_key=True,  default=uuid.uuid1().int>>64, unique=True, editable=False)
    title =  models.CharField(max_length=50)
    category=  models.CharField(max_length=50)
    content =  models.TextField(blank=True, null=True)
    image =  models.CharField(max_length=100)
    date_published =  models.DateTimeField(auto_now_add=True)
    author =  models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.IntegerField()
    likes =  models.IntegerField()



    def str(self):
        return self.id

