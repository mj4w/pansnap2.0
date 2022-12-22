
from multiprocessing import reduction
from urllib.parse import non_hierarchical
from wsgiref.util import request_uri
from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User , auth

# Create your views here.
def home(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request,'hi')
                return redirect('home')
            else:
                messages.warning(request,'Credentials Invalid')
        else:
            messages.warning(request,'Username and Password Incorrect!')
    form = AuthenticationForm()
    context ={
        'form':form,
    }
    return render(request,'home.html', context)

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request, 'services.html')

def hire_us(request):
    return render(request, 'hire_us.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def contact(request):
    return render(request, 'contact.html')

def signup(request):
    if request.method == "POST":
        username= request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
                return redirect(request.META['HTTP_REFERER'])
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username already exists')
                return redirect(request.META['HTTP_REFERER'])
            else:
                user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
                user.save()
                #login
                login_user = auth.authenticate(username=username, password=password)
                auth.login(request, login_user)
                return redirect('home')
        else:
            messages.info(request,'Password Not Match')
            return redirect(request.META['HTTP_REFERER'])

            


    return render(request,'sign-up.html')


def logout_user(request):
    logout(request)
    messages.info(request, 'Thankyou for visiting')
    return redirect('home')

