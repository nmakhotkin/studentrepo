#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import auth
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from student.accounts import forms
from student.shortcuts import render_to_response


def login(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # Пароль верный и пользователь активен
            auth.login(request, user)
            # Переадресация на страницу
            return HttpResponseRedirect("/")
        else:
            context['errors'] = 'Incorrect'
            form = forms.LoginForm()
            context['form'] = form
    else:
        form = forms.LoginForm()
        context['form'] = form

    context['title'] = "Login"
    context.update(csrf(request))

    return render_to_response("accounts/login.html", context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("account/loggedout/")


def registration(request):
    context = {}
    if request.method == "POST":
        post_data = request.POST
        username = post_data.get('username', '')
        password = post_data.get('password', '')
        email = post_data.get('email', '')
        first_name = post_data.get('first_name', '')
        last_name = post_data.get('last_name', '')

        User.objects.create_user(username, email, password,
                                 first_name=first_name,
                                 last_name=last_name)

        return HttpResponseRedirect("/")

    else:
        form = forms.RegistrationForm()
        context['form'] = form

    context['title'] = "Login"
    context.update(csrf(request))

    return render_to_response("accounts/registration.html", context)


def profile(request):
    if request.user.is_authenticated():
        context = {'user': '1'}
    else:
        context = {'user': '0'}

    context.update(csrf(request))

    return render_to_response("accounts/profile.html", context)
