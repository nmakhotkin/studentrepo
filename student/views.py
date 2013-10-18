#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.context_processors import csrf # для загрузки файлов
from datetime import datetime


def home(request):

    params = {}

    params['time'] = (datetime.now().strftime('%H:%M:%S'))
    params['date'] = (datetime.now().strftime('%Y-%m-%d'))

    params.update(csrf(request))
    return render_to_response('index.html', params)