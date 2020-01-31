from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def accountSign(request):
    return HttpResponse('hello to sign in up page')
