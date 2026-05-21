from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignUPForm

# Create your views here.


def signup_action(req):
    if req.method == "POST":
        form = SignUPForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return HttpResponse('Failed to save the data')
    else:
        form = SignUPForm()
        return render(req, "signup/signup.html", {'form': form})
