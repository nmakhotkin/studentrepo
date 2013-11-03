#!/usr/bin/env python
# -*- coding: utf-8 -*-

from student.shortcuts import render_to_response
from django.core.context_processors import csrf  # для загрузки файлов
from datetime import datetime


def home(request):

    params = {}
    params['time'] = (datetime.now().strftime('%H:%M:%S'))
    params['date'] = (datetime.now().strftime('%Y-%m-%d'))

    params['author'] = 'STRATEG'

    lst = []

    for i in xrange(1, 20):
        lst.append({"index": i})

    params['items'] = lst

    params['static'] = 'static/'

    params['title'] = "Test title"

    params['error'] = ""

    params['path'] = ''

    # params.update(csrf(request))
    params["csrftoken"] = csrf(request)["csrf_token"]
    return render_to_response('index.html', params)
