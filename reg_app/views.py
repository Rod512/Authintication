from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login 
from .forms import regForm , loginForm
from .models import user

def home(request):
    if request.method == 'POST':
     fm = regForm(request.POST)
     if fm.is_valid():
        nm = fm.cleaned_data['name']
        em = fm.cleaned_data['email']
        pw = fm.cleaned_data['password']
        rpaw = fm.cleaned_data['retype_pass']
        reg = user(name = nm, email = em, password = pw, retype_pass = rpaw )
        reg.save()
        return HttpResponseRedirect('/login/auth')  
        

    else:
     fm = regForm()
    return render(request, 'reg_app/index.html', {'form': fm} )

def login(request):
    if request.method == 'POST':
        loginfm = loginForm(request.POST)
        if loginfm.is_valid():
            email = loginfm.cleaned_data['email']
            password = loginfm.cleaned_data['password']
            user_data = authenticate(request, email = email, password = password)
            if user_data is not None:
               login(request, user_data)
               return HttpResponseRedirect('/home/home_page')
            else:
               return HttpResponse('Problem')
               
    loginfm = loginForm()
    return render(request, 'reg_app/login.html', {'form': loginfm})


def homepage(request):
   return render(request, 'reg_app/home.html')