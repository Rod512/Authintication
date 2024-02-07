from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import regForm

def home(request):
    if request.method == 'POST':
        fm = regForm(request.POST)
        if fm.is_valid():
            print('from validated')
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            retype_pass = fm.cleaned_data['retype_pass']
            print("name", name)
            print("email", email)
            print('pass', password)
            print('rePAss', retype_pass)
            return HttpResponseRedirect('/login/auth')
            
    else:
        fm = regForm()
    return render(request, 'reg_app/index.html', {'form':fm} )

def login(request):
    return render(request, 'reg_app/login.html')