"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from signup.views import signaction,home
from login.views import loginaction,logout_user
from display.views import newrecord

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/",home,name='home'),
    path("signup/",signaction,name='signaction'),
    path("login/",loginaction,name='loginaction'),
    path("newrecord",newrecord,name='newrecord'),
    path('logout/',logout_user,name='logout')
]
