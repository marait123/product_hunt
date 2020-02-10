from . import views
from django.urls import path
urlpatterns = [
    path('',views.home, name = 'home'),
    path('create/',views.createProduct, name = 'createProduct'),
    path("<int:prodId>/", views.details, name="details"),
]
