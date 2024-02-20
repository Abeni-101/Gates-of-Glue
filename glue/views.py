from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .form import User_Creation_Form
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *


def register_account(request):
    if request.method=="POST":
         username=request.POST["username"]
         email=request.POST["email"]
         password1=request.POST["password1"]
         password2=request.POST["password2"]
         if password1==password2:
             if User.objects.filter(email=email).exists():
                 messages.info(request,"this email is already registered")
                 return redirect("register")
             elif User.objects.filter(username=username).exists():
                 messages.info(request,"username already taken")

             else:
                 user=User.objects.create_user(username=username,email=email,password=password1)
                 user.save()
                 return redirect("login")
         else:
             messages.info(request,"passwords are not matching")
             return redirect("register")
         
    return render(request,"glue/register.html")


def login_account(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"invalid credentials")
            return redirect("login")
    return render(request,"glue/login.html")
def logoutuser(request):
    logout(request)
    return redirect("/login")
@login_required(login_url='login')
def home(request):
    lists=Todo.objects.filter(user=request.user)
    wish=Wish.objects.filter(user=request.user)
    if request.method=="POST":
        input_text=request.POST["input-list"]
        radio_btn=request.POST["radio"]
        if radio_btn=="todo":
           ins=Todo.objects.create(user=request.user,todo_list=input_text)
           ins.save()
           return redirect("/")
        elif radio_btn=="wish":
            ins=Wish.objects.create(user=request.user,wish_list=input_text)
            ins.save()
            return redirect("/")
    context={"lists":lists , "wish":wish}
    return render(request,"glue/home.html",context)
def update_todo_list(request,pk):
    update_todo=Todo.objects.get(id=pk)
    if request.method=="POST":
        update_todo.todo_list=request.POST["input-list"]
        update_todo.save()
        return redirect("/")
    return render(request,"glue/update.html",{"update_todo":update_todo,})
def update_wish_list(request,pk):
    update_wish=Wish.objects.get(id=pk)
    if request.method=="POST":
        update_wish.wish_list=request.POST["input-list"]
        update_wish.save()
        return redirect("/")
    return render(request,"glue/update-wish.html",{"update_wish":update_wish,})
def delete_todo_obj(request,pk):
    obj_delete=Todo.objects.get(id=pk)
    obj_delete.delete()
    return redirect("/")
def delete_wish_obj(reqest,pk):
    obj_delete=Wish.objects.get(id=pk)
    obj_delete.delete()
    return redirect("/")


    



