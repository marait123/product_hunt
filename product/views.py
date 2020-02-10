from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpRequest
from .models import Product
from django.contrib.auth.decorators import login_required

from django.utils import timezone
# Create your views here.
def home(request):
    print("u are home")
    products = Product.objects.all()
    return render(request, 'product/home.html',{'products':products})

@login_required
def createProduct(request:HttpRequest):

    if request.method == "POST":
        if request.POST['title'] and request.POST['url'] and request.POST['body'] and request.FILES['image'] and request.FILES['icon']:
            print("adding the product")
            prod = Product()
            prod.title = request.POST['title']
            prod.body = request.POST['body']

            if request.POST['url'].startswith('https://') or  request.POST['url'].startswith('http://') :
                prod.url = request.POST['url']
            else:
                prod.url = 'http://' + request.POST['url']
            prod.icon = request.FILES['icon']
            prod.image = request.FILES['image']
            prod.pub_date = timezone.datetime.now()
            prod.hunter = request.user
            prod.save()

            return render(request, 'product/createProduct.html', {'error':'product was created successfully'})

        else:
            return render(request, 'product/createProduct.html', {'error':'error all the fields are required'}) 
    else:
        return render(request, 'product/createProduct.html')
def details(request:HttpRequest, prodId):
    #Prod = get_object_or_404(Product, pk = prodId)
    Prod = Product.objects.filter(id  = prodId)
    print(prodId)
    print(Prod)
    return render(request, 'product/detail.html', {'product':Prod[0]})