from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout

def new_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request,form.save())
            return redirect("/")
    else:
        form = UserCreationForm()
    return render(request,"user/register.html",{'form':form})

def new_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            login(request,form.get_user())
            return redirect("/")

    else:
        form = AuthenticationForm()

    return render(request,"user/login.html",{'form':form})

def logout(request):
    if request.method=="POST":
        logout(request)
        return redirect("/")