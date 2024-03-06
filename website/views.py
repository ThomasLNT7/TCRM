from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def home(request):
    #check login
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        #authentification
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Vous êtes bien connecté !")
            return redirect('home')
        else:
            messages.success(request, "Il y a eu une erreur, reconnectez vous :x !")
            return redirect('home')
    else:
        return render(request, "home.html", {})

def logout_user(request):
    logout(request)
    messages.success(request, "Vous vous êtes bien déconnecté")
    return redirect('home')

def register_user(request):
    return render(request, "register.html", {})
