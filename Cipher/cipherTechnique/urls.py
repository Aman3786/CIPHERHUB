from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('playfair',views.playfair,name='playfair'),
    path('ceasar',views.ceasar,name='ceasar'),
    path('rsa',views.rsa,name='rsa'),
    # path('encrypt',views.encrypt,name='encrypt'),
]