from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views import generic
from datetime import date
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib import messages, auth
from django.db.models import Q
from .models import Account


# Verification email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage

# Create your views here.


def login(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user:
            auth.login(request, user)
            messages.success(request, f'Welcome!')
            return redirect('Menu')
        else:
            messages.error(
                request, 'credential seen to be wrong,check the credential and please try again!')
            return redirect('Login')

    return render(request, 'accounts/login.html')


@login_required(login_url='Login')
def logout(request):
    auth.logout(request)
    messages.success(request, f'Have a nice day :)')
    return redirect('Login')


@login_required(login_url='Login')
def menu(request):
    if request.user.is_authenticated:

        return render(request, 'accounts/menu.html')
    else:
        messages.error(request, 'Access Denied!')
        return redirect('Login')
