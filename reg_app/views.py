from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login 
from .forms import regForm , loginForm
from .models import User

def home(request):
    if request.method == 'POST':
     fm = regForm(request.POST)
     if fm.is_valid():
        nm = fm.cleaned_data['name']
        em = fm.cleaned_data['email']
        pw = fm.cleaned_data['password']
        rpaw = fm.cleaned_data['retype_pass']
        reg = User(name = nm, email = em, password = pw, retype_pass = rpaw )
        reg.save()
        return HttpResponseRedirect('/login/auth')  
        

    else:
     fm = regForm()
    return render(request, 'reg_app/index.html', {'form': fm} )

def user_login(request):
    if request.method == 'POST':
        loginfm = loginForm(request.POST)
        if loginfm.is_valid():
            email = request.POST.get('login_email')
            password = request.POST.get('login_pass')
            print(email,password)
            user = User.objects.get(email= email, password = password)
            print(user)
            return HttpResponseRedirect('/home/home_page')
        else:
           HttpResponseRedirect('/login/auth')
            
               
    loginfm = loginForm()
    return render(request, 'reg_app/login.html', {'form': loginfm})


   


def homepage(request):
   return render(request, 'reg_app/home.html')