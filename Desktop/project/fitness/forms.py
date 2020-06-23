from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,PasswordResetForm
from django.contrib.auth.models import User
from .models import Goal

class GoalForm(forms.ModelForm):
    #goalform = forms.CharField(max_length=1000)
    
    class Meta:
        model = Goal
        fields=['goal']
class PasswordResetForm(forms.Form):
    email = forms.CharField(max_length=100 , widget=forms.EmailInput(attrs={'class':"form-control rounded text-center w-75 mx-auto",'style':"font-family:OratorStd;",'placeholder':'EMAIL'}))
    class Meta:
        fields=['email']
    

    
    

    


class CreateUserForm(UserCreationForm):
    username = forms.CharField(max_length=100 , widget=forms.TextInput(attrs={'class':"form-control rounded text-center w-75 mx-auto",'style':"font-family:OratorStd;",'placeholder':'USERNAME'}))
    email = forms.CharField(max_length=100 , widget=forms.EmailInput(attrs={'class':"form-control rounded text-center w-75 mx-auto",'style':"font-family:OratorStd;",'placeholder':'EMAIL'}))
    password1 = forms.CharField(max_length=100 , widget=forms.PasswordInput(attrs={'class':"form-control rounded text-center w-75 mx-auto",'placeholder':'PASSWORD','style':"font-family:OratorStd;"}))
    password2 = forms.CharField(max_length=100 , widget=forms.PasswordInput(attrs={'class':"form-control rounded text-center w-75 mx-auto",'placeholder':'CONFIRM PASSWORD','style':"font-family:OratorStd;"}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

