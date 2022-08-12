from django.shortcuts import render
from pizza.models import *
from django.shortcuts import  render, redirect
from .forms import NewUserForm, UserLoginForm
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm


def index(request):
    Pizzas = Pizza.objects.all()
    Sushis = Sushi.objects.all()
    Zakuskas = Zakuska.objects.all()
    Desserts = Dessert.objects.all()
    Juices = Juice.objects.all()
    Sauces = Sauce.objects.all()
    Combos = Combo.objects.all()

    context = {
        'pizza': Pizzas,
        'sushi': Sushis,
        'zakuska': Zakuskas,
        'dessert': Desserts,
        'juice': Juices,
        'sauce': Sauces,
        'combo': Combos,
    }
    return render(request, 'index.html', context)


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("index")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name='register.html', context={"register_form":form})


def login_request(request):
    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("index")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = UserLoginForm()
    return render(request=request, template_name="login.html", context={"login_form":form})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
	return redirect("index")

def cart(request):
    return render(request, 'cart.html')










