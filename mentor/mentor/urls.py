"""
URL configuration for mentor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home", views.index, name="index"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("details", views.details, name="details"),
    path("ss", views.ss, name="ss"),
    path("courses", views.courses, name="courses"),
    path("downloads", views.downloads, name="downloads"),
    path("bca", views.bca, name="bca"),
    path("bba", views.bba, name="bba"),
    path("ba", views.ba, name="ba"),
    path("bcom", views.bcom, name="bcom"),
    path("bsc", views.bsc, name="bsc"),
    path("ma", views.ma, name="ma"),
    path("mcom", views.mcom, name="mcom"),
    path("msc", views.msc, name="msc"),
    path("bva", views.bva, name="bva"),
]
