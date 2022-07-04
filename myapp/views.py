from django.shortcuts import redirect, render
from requests import get

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
