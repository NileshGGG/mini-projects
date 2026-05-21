from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import LoginForm

# Create your views here.

#web browser -> views.py -> fuction -> renders the webpage

def login_action(req):
    if req.method == "POST":
        form = LoginForm(req.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']

            user = authenticate(req, username=u, password=p)


            if user:
                login(req, user)
                return redirect('welcome')
            else:
                return redirect('error')

        else:
            return HttpResponse('Failed to save the data !!')
        
    else:
        form = LoginForm()
        return render(req, "login/login.html", {'form': form})
    

def logout_action(req):
    logout(req)
    return redirect('login')


def welcome(req):
    return render(req, "login/welcome.html")

def error(req):
    return render(req, "login/error.html")
