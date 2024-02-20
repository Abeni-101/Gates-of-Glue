from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Todo
class User_Creation_Form(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2"]
        