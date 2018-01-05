# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import UserMessage


def getTest(request):
    if (request.method == 'POST'):
        data = {}
        data['name'] = request.POST.get('name')
        data['email'] = request.POST.get('email')
        data['address'] = request.POST.get('address')
        data['message'] = request.POST.get('message')
        userMessage = UserMessage()
        userMessage.name = data['name']
        userMessage.email = data['email']
        userMessage.address = data['address']
        userMessage.message = data['message']
        userMessage.save()
        return HttpResponse('success')
    return render(request, 'messageboard.html')
