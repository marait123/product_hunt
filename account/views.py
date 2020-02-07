from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpRequest
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.

def logIn1(request:HttpRequest):
    print("hello log in")
    if(request.method == 'POST'): 
        print("entered post region")
        try:            
            user:User = User.objects.get(username = request.POST['userName'])
            print(user.username)
            print(user.password)
            if request.POST['password'] == user.password:
                return render(request, 'logIn.html',{'error':'you are logged in'})
            else:
                return render(request, 'signUp.html',{'error':'password incorrect'})
        except User.DoesNotExist:
            return render(request, 'signUp.html',{'error':'incorrect user name'})
        except:
            return render(request, 'signUp.html',{'error':'incorrect user name'})

        
    else:
        #user wants to enter info
        return render(request, 'logIn.html',{'error':'normal operation'})

    

def logIn(request:HttpRequest):
    print("hello log in")
    if(request.method == 'POST'): 
        user:User = auth.authenticate(username = request.POST['userName'], password = request.POST['password'])
        
        if user is not None:
            auth.login(request, user)
            return render(request, 'product/home.html',{"user":user})
        else:
            return render(request, 'signUp.html',{'error':'password or username incorrect'})
     
    else:
        #user wants to enter info
        return render(request, 'logIn.html',{'error':'login test'})

    

def signUp(request:HttpRequest):
    print("hello signUp")
    if(request.method == 'POST'): 
        print("entered post region")
        try:            
            if request.POST['password'] == request.POST['confirmPassword']:
                user = User.objects.get(username = request.POST['userName'])           
                return render(request, 'signUp.html',{'error':'user name already exists'})
            else:
                return render(request, 'signUp.html',{'error':'tow passwords aren\'t identical'})

        except User.DoesNotExist:    
            user = User.objects.create_user(request.POST['userName'], password=request.POST['password'])
            auth.login(request,user)
            return redirect('home')
        except:
            return render(request, 'signUp.html',{'error':'normal operation'})

        
    else:
        #user wants to enter info
        return render(request, 'signUp.html',{'error':'normal operation'})
def logOut(request:HttpRequest):
    # TODO need to route to home page
   
    #if request.method == "POST":
    print("logging out")
    auth.logout(request)
    return render(request, 'logOut.html')
