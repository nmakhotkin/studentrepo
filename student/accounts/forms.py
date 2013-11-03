#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from student.models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class RegistrationForm(forms.Form):
    username = forms.CharField(label="Имя пользователя")
    password = forms.CharField()
    check_password = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = (
            "birth_date",
            "short_description",
            "programming_languages")
