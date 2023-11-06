from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as login1
from django.contrib.auth import logout as log
from django.db import IntegrityError
from django.shortcuts import redirect
# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request,'login.html',{'form':AuthenticationForm})
    else:
        user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'login.html',{'form':AuthenticationForm(),'error':'username and password do not match'})
        else:
            login1(request,user)
            return redirect('/')
def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html',{'form':UserCreationForm})
    else:
        if request.POST['password1']==request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login1(request,user)
                return redirect('/')
            except IntegrityError:
                return render(request,'signup.html',{'form':UserCreationForm,'error':'Username Already Exist'})
        else:
            return render(request,'signup.html',{'form':UserCreationForm,'error':'password must be same'})
def logout(request):
    log(request)
    return redirect('/')
            
