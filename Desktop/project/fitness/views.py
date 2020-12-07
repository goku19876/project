# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,PasswordResetForm
from .forms import CreateUserForm,ModelForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,get_user
from django.contrib.auth.decorators import login_required
from .forms import GoalForm,RoutineForm,PhoneForm
from .models import Goal, Routine
from plotly.offline import plot
import plotly.graph_objs as go
from plotly.graph_objs import Scatter
from django.shortcuts import get_object_or_404
from twilio.rest import Client

# Create your views here.
def routine(request):
    form = RoutineForm()
    if request.method=="POST":
        form = RoutineForm(request.POST)
        form.instance.user = request.user
        form.save()
    context={
        'routineForm':form,
        'user':request.user
    }
    
    return render(request,'fitness/routine.html',context)
def customizeRoutine(request,routine_id):
    form = Routine.objects.filter(id=routine_id)
    if request.method =="POST":
        pass
        
    context={

    }
    render(request,'fitness/routine.html',context)
@login_required
def home(request):
    
            
    form = GoalForm()
    all_goals = Goal.objects.filter(user = request.user)
    routine = Routine.objects.filter(user=request.user)
    phone=PhoneForm()
    
    if request.method =='POST' and 'submit_goal' in request.POST:
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
    if request.method=='POST' and 'submit_number' in request.POST:
        
        account_sid = "ACd201f574e9f63cbe8aca15e13011e383"
        auth_token  = "00215b58f89df15c249b1c48f3db4a19"
        client = Client(account_sid, auth_token)
        number=request.POST.get('phonenumber')
        text = request.POST.get('text')
        message = client.messages.create(
            to=number, 
            from_="+12055095109",
            body=text)
    
    
    context={
        'form':form,
        'user':request.user,
        'goal':all_goals,
        'routine':routine,
        'phone':phone,
    }
    return render(request,'fitness/home.html',context)

def deleteGoal(request,goal_id):
    
    if request.method =="POST" :
        goal = Goal.objects.get(id=goal_id)
        goal.delete()


    return redirect('home')
    

        
    


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