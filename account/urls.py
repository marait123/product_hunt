from . import views
from django.urls import path
urlpatterns = [
    path('login/',views.logIn, name = 'logIn'),
    path('signup/',views.signUp, name = 'signUp'),
    path('logout/',views.logOut, name = 'logOut'),


]
