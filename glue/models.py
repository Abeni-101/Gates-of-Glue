from django.db import models
from django.contrib.auth.models import User
#you can also use get_user_model() function instead of User 
#from django.contrib.auth import get_user_model
#user=get_user_model()

class Todo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    todo_list=models.CharField(max_length=100,blank=True)
    added_date=models.DateTimeField(null=True,blank=True)
    def __str__(self):
        return self.user.username
class Wish(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    wish_list=models.CharField(max_length=100,blank=True)
    added_date=models.DateTimeField(null=True,blank=True)
    def __str__(self):
        return self.user.username


# Create your models here.
