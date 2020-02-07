from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    print("u are home")
    return render(request, 'product/home.html')