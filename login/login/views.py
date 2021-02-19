from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "home.html")

@login_required
def logoutPage(request):
    logout(request)
    return render(request, "home.html", {})

def loginPage(request):
    template_name = "login.html"
    context = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')  
        else:
            print("error")
            messages.info(request, "Username or password is incorrect")
    return render(request, template_name, context)

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        try:
            if form.is_valid:
                form.save()
                messages.success(request, "Account was created!")
                return redirect('/login/')
        except:
            return HttpResponse("<h1>Username or email already exist</h1>")
    context = {'form':form}
    template_name = "register.html"
    return render(request, template_name, context)

def contact(request):
    print(request.POST)
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        return redirect('/blog')
    context = {'title':'Contact us','form':form}
    return render(request, "form.html", context)

def about(request):
    template_name = "about.html"
    context = {}
    return render(request, template_name, context)