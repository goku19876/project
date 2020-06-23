# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,PasswordResetForm
from .forms import CreateUserForm,ModelForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,get_user
from django.contrib.auth.decorators import login_required
from .forms import GoalForm
from .models import Goal
from plotly.offline import plot
import plotly.graph_objs as go
from plotly.graph_objs import Scatter
# Create your views here.
@login_required
def home(request):
    form = GoalForm(initial={'user':request.user})
    all_goals = Goal.objects.filter(user = request.user)
    

    
                        
                    

    if request.method =='POST':
        form = GoalForm(request.POST)
        
        if form.is_valid():
            
            form.save(commit=False)
            form.instance.user = request.user
            form.save()
            messages.success(request,"Updated goals!")
            return redirect('home')
        else:
            form = GoalForm()
            return redirect('home')
        



    context={'form':form,'user':request.user,'goal':all_goals}
    return render(request,'fitness/home.html',context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,"incorrect credentials")
    return render(request,'fitness/login.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = CreateUserForm()
    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"user created succesfully for {username}".format(username = form.cleaned_data.get('username')))
            return redirect('login')

    context= {
        'form':form
    }
    return render(request,'fitness/register.html',context)

def default(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request,'fitness/default.html')
    
def testform(request):
    
    return render(request,'fitness/testform.html')

def logoutUser(request):
    logout(request)
    return redirect('login')