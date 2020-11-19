from django.shortcuts import render
from taskapp import models
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from taskapp.models import Car
from django.shortcuts import redirect
# Create your views here.
def Home(request):
    return render(request, 'home.html')

def Alto(request):
    return render(request, 'alto.html')

def Maruti(request):
    return render(request, 'maruti.html')

def Jaguar(request):
    return render(request, 'jaguar.html')

def Login(request):
    return render(request, 'login.html')

def Signup(request):
    return render(request, 'signup.html')

def add(request):
    if request.method == 'POST':
        form = request.POST
        car=models.Car()
        car.Name=form.get('Name')
        car.Phone=form.get('Phone')
        car.Email=form.get('Email')
        car.Password=form.get('Password')
        car.save()
    return HttpResponseRedirect('/')

def Logout(request):
    request.session.clear()
    return redirect('login')

 
def Login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        customer = Car.get_customer_by_email(Email)
        error_message = None
        if customer:
            flag = check_password(Password , customer.Password)
            if flag:
                return redirect('/')
            else:
                error_message = 'Email or Password Invalid'
        else:
            error_message = 'Email or Password Invalid'
        return render(request, 'login.html', )

