# -*- coding: utf-8 -*-
# Views of your app.

from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'base/index.html', context)
