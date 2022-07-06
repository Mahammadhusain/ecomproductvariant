from django.shortcuts import redirect, render
from django.http import JsonResponse
from requests import get, request
from validators import card_number

from myapp.models import *

# Create your views here.


def HomeView(request):
    all_prod = ProductNameModel.objects.all()
    
    if request.method == 'POST':
        get_price = request.POST.get('var')
        get_quantity = request.POST.get('quantity')
        print(int(get_price)*int(get_quantity))
        return redirect('/')
    else:

        context = {
            'all_prod': all_prod
        }
        return render(request, 'index.html', context)


def Add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('var')
        get_product = ProductModel.objects.get(id=product_id)
        product_quantity = request.POST.get('quantity')
        if CartModel.objects.filter(product = get_product).exists():
            cart_product = CartModel.objects.get(product = get_product)
            cart_product.quantity = int(cart_product.quantity)+int(product_quantity)
            cart_product.save()
        else:
            CartModel(user=request.user,product=get_product,quantity =product_quantity).save()

        
        return redirect('/')
    else:pass

def ShowcartView(request):
    cart_items = CartModel.objects.all()
    context = {'cart_items':cart_items}
    return render(request,'cart.html',context)


def UpdatecartView(request):
    if request.method == 'POST':
        get_prod_id= request.POST.getlist('prod_id')
        get_prod_qua= request.POST.getlist('prod_qua')[::-1]
        card_items= CartModel.objects.filter(product_id__in = get_prod_id)
        for i in range(len(card_items)):
            card_items[i].quantity = get_prod_qua[i] 
            card_items[i].save()
    return redirect('/showcart/')