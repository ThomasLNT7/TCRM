from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record


# Create your views here.
def home(request):
    records = Record.objects.all()

    # check login
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # authentification
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Vous êtes bien connecté !")
            return redirect('home')
        else:
            messages.success(request, "Il y a eu une erreur, reconnectez vous :x !")
            return redirect('home')
    else:
        return render(request, "home.html", {'records': records})


def logout_user(request):
    logout(request)
    messages.success(request, "Vous vous êtes bien déconnecté")
    return redirect('home')


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Vous êtes bien enregistré !")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, "register.html", {'form': form})

    return render(request, "register.html", {'form': form})

def search_bar(request):
    if request.method == "POST":
        searched = request.POST["searched"]

        return render(request, "search_result.html", {"searched": searched})
    else:
        return render(request, "search_result.html", {})
