from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [

    path('login/', views.login, name='Login'),

    path('logout/', views.logout, name='Logout'),

    path('menu/', views.menu, name='Menu'),

]
