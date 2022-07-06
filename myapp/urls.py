from django.urls import path
from .views import *
 
urlpatterns = [
 
    path('', HomeView,name='home'),
    path('add_to_cart/', Add_to_cart,name='add_to_cart'),
    path('showcart/', ShowcartView,name='showcart'),
    path('updatecart/', UpdatecartView,name='updatecart'),
 
]
