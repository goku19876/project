"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views
from forms import PasswordResetForm
from django.shortcuts import get_object_or_404

urlpatterns = [
    url('home',views.home,name="home"),
    url('login',views.loginPage,name="login"),
    url('register',views.register,name="register"),
    url('reset_password/',auth_views.PasswordResetView.as_view(template_name='fitness/resetpw.html'),name="reset_password"),
    url('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='fitness/resetpw_sent.html'), name="password_reset_done"),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    url('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
    url(r'delete/(?P<goal_id>[\S]+)', views.deleteGoal, name='deleteGoal'),
    url('logout', views.logoutUser,name="logoutPage"),
    url('routine', views.routine,name="routinePage"),
    url(r'routine/(?P<routine_id>[\S]+)', views.customizeRoutine, name='customizeRoutine'),
    url('',views.default,name="default"),
    

]
